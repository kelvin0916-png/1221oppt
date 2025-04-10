import click
from subdomain_finder import find_subdomains
from live_checker import is_alive
from crawler import crawl

@click.group()
def cli():
    """Command-line interface for domain-related tasks."""
    pass

@cli.command()
@click.argument('domain')
def enum(domain):
    """Enumerates subdomains for a given domain."""
    subs = find_subdomains(domain)
    for sub in subs:
        print(sub)

@cli.command()
@click.argument('domain')
def check(domain):
    """Checks the live status of subdomains for a given domain."""
    subs = find_subdomains(domain)
    for sub in subs:
        if is_alive(sub):
            print(f"[✅ LIVE] {sub}")
        else:
            print(f"[❌ DEAD] {sub}")

@cli.command()
@click.argument('url')
@click.option('--depth', default=2, help='Depth to crawl')
@click.option('--output', default=None, help='Save links to a CSV file')
def spider(url, depth, output):
    """Crawls a URL for data extraction or other purposes."""
    from crawler import crawl
    crawl(url, depth=depth, output_file=output)

if __name__ == "__main__":
    cli()
print("Testing push to GitHub!")  # Just added this
