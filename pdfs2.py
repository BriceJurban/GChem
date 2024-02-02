import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_links_from_page(url):
    """
    Extract all valid URLs from the given page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting all links from the page
    links = [urljoin(url, link.get('href')) for link in soup.find_all('a')]

    # Filter only links that lead to the same domain
    domain = urlparse(url).netloc
    valid_links = [link for link in links if urlparse(link).netloc == domain]

    return valid_links

def get_all_pdf_links(url):
    """
    Get all PDF links from a given URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting all links that might point to PDFs
    potential_links = [urljoin(url, link.get('href')) for link in soup.find_all('a') if 'pdf' in link.get('href', '').lower()]

    return potential_links

def download_pdf_from_link(pdf_url, dest_folder="."):
    """
    Download a PDF from the given URL and save it to the specified destination folder.
    """
    response = requests.get(pdf_url, stream=True)
    response.raise_for_status()

    local_filename = os.path.join(dest_folder, pdf_url.split('/')[-1])
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Downloaded: {pdf_url} -> {local_filename}")

def download_pdfs_from_multiple_urls(main_url, dest_folder="."):
    """
    Download all PDFs from all URLs found on the main_url page.
    """
    all_links = get_all_links_from_page(main_url)

    # For each link found on the main page, check for PDFs and download them
    for link in all_links:
        pdf_links = get_all_pdf_links(link)
        for pdf_link in pdf_links:
            download_pdf_from_link(pdf_link, dest_folder)

if __name__ == "__main__":
    main_url = input("Enter the main URL: ")
    dest_folder = input("Enter the destination folder (default: current directory): ") or "."
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    download_pdfs_from_multiple_urls(main_url, dest_folder)
