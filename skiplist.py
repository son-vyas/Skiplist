import requests
import os

RELEASES = ['master']
JOB_NAME = 'periodic-tripleo-ci-centos-7-ovb-1ctlr_2comp-featureset021-'
ZUUL_API_BUILD = 'https://review.rdoproject.org/zuul/api/builds?job_name='
TEMPEST_LOG = 'logs/tempest.html.gz'
TEMPEST_DUMP_DIR = '/tmp/skip'


def get_last_build():
    """
    This Fuction is used to get the lastest information about master-release.
    return the zuul_job_url with the help of zuul_api_build and job_name
    store complete log_url, download tempest.html.gz file at /tmp/skip
    """
    for release in RELEASES:
        zuul_job_url = '{}{}{}'.format(ZUUL_API_BUILD, JOB_NAME, release)
        resp = requests.get(zuul_job_url)
        if resp.status_code == 200:
            zuul_log_url = resp.json()[0]['log_url']
            tempest_log_url = '{}{}'.format(zuul_log_url, TEMPEST_LOG)
            if requests.get(tempest_log_url).status_code == 200:
                if not os.path.exists(TEMPEST_DUMP_DIR):
                    os.mkdir(TEMPEST_DUMP_DIR)
                file_name = download_tempest_file(
                    tempest_log_url, TEMPEST_DUMP_DIR)
                print(file_name)


def download_tempest_file(url, local_dir):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join(local_dir, local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
    return local_filename


if __name__ == "__main__":
    get_last_build()
