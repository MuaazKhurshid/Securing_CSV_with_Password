import zipfile
import pyzipper

from models.importer import ROOT_DIR, logger

def create_csv_content(csv_name):
    logger.info("Generating some CSV Content.")
    csv_content = "Name,Age\nNameA,20\nNameB,30\nNameC,40"
    with open(csv_name,'w+') as csv_file:
        csv_file.write(csv_content)
    logger.info("Sample CSV Data has been Generated")


def protect_csv(csv_name, zip_file_name, password):
    try:
        csv_file_path = f"{ROOT_DIR}\\data_source_'1'\\{csv_name}"
        zip_file_path = f"{ROOT_DIR}\\data_target_'1'\\{zip_file_name}"

        with pyzipper.AESZipFile(zip_file_path, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zipf:
            zipf.setpassword(password.encode())
            zipf.write(csv_file_path, csv_name)
            logger.info("CSV File has been protected with Password")
    except Exception as prtct_csv_Exc:
        logger.error(f'Exception in models\secure_csv\protect_csv: {prtct_csv_Exc}')
