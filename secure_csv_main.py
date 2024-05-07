from models.importer import logger, ROOT_DIR
from models.secure_csv import create_csv_content, protect_csv



if __name__ == '__main__':
    logger.info('Welcome to CSV Securer Script')
    csv_name  = 'sample_data.csv'
    zip_file_name = 'sample_data.zip'
    # create_csv_content(csv_name=csv_name)
    protect_csv(csv_name=csv_name, zip_file_name=zip_file_name, password='my_pass')


