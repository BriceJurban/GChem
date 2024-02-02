import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_pdf_links(url):
    """
    Get all PDF links from a given URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links that ends with .pdf
    pdf_links = [urljoin(url, link.get('href')) for link in soup.find_all('a') if link.get('href', '').endswith('.pdf')]

    return pdf_links

def download_pdf_from_link(pdf_url, dest_folder="."):
    """
    Download a PDF from the given URL and save it to the specified destination folder.
    """
    response = requests.get(pdf_url, stream=True)

    # Check if the request was successful
    response.raise_for_status()

    # Write content to a .pdf file
    local_filename = os.path.join(dest_folder, pdf_url.split('/')[-1])
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Downloaded: {pdf_url} -> {local_filename}")

def download_pdfs_from_url(url, dest_folder="."):
    """
    Download all PDFs from a given URL to the specified destination folder.
    """
    pdf_links = get_all_pdf_links(url)
    for link in pdf_links:
        download_pdf_from_link(link, dest_folder)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    dest_folder = input("Enter the destination folder (default: current directory): ") or "."
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    download_pdfs_from_url(url, dest_folder)
