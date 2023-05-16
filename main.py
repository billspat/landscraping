import google_streetview.api
import os

def has_sv(results):
    return( not results.metadata[0]['status']=='NOT_FOUND' )

SV_STD_FILENAME='gsv_0.jpg'

def base_file_name(lat, lon, prefix=''):
    return(f"{prefix}{lat}_{lon}")

def img_file_location(lat, lon, image_path = "images"):
    download_dir = os.path.join(image_path,base_file_name(lat, lon))
    return(download_dir)

def get_image(lat,lon,fov='20', image_path = 'images', gkey = None):
    # Define parameters for street view api
    gkey = gkey or os.getenv('GKEY')
    params = [{
        'size': '640x640',
        'location': f"{lat},{lon}",
        'fov' : fov,
        'key': gkey
    }]
    download_dir = os.path.join(image_path,base_file_name(lat, lon))
    # Create a results object
    results = google_streetview.api.results(params)
    if has_sv(results):
        # Download images to directory 'downloads'
        results.download_links(download_dir)
        results.save_metadata(f"metadata_{base_file_name(lat, lon)}.json")
        return(True)
    else:
        return(False)




def test_locations(gkey=None, image_path = "testimages"):
    # on trail
    fov=20
    lat,lon = 1.3812733452743484, 103.81803299353679
    get_image(lat,lon,fov,image_path, gkey)
    # fewer digits
lat,lon = 1.381273345274348, 103.8180329935367
    get_image(lat,lon,fov,image_path, gkey)