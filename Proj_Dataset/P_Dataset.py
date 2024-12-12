from bing_image_downloader import downloader

#bx as imgs de gatos
downloader.download("cat", limit=100, output_dir="database_cat", adult_filter_off=True, force_replace=False, timeout=120)

#bx as imgs de cachorros
downloader.download("dog", limit=100, output_dir="database_dog", adult_filter_off=True, force_replace=False, timeout=120)

print("Download concluido!")