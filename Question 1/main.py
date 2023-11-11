import mysql.connector as connector
import logging
import configparser

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(asctime)s - %(message)s")
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class DBHelper:
    def __init__(self, config_file: str = "config.ini"):
        """
        Initialize the DBHelper instance.

        :param config_file: Path to the configuration file (default: 'config.ini')
        """

        self.config = self.load_config(config_file)
        self.con = connector.connect(**self.config["database"])

    def load_config(self, config_file: str):
        """
        Load configuration settings from a file.

        :param config_file: Path to the configuration file.
        :return: A configparser.ConfigParser instance.
        """

        config = configparser.ConfigParser()
        config.read(config_file)
        return config

    def fetch_all_departments(self):
        """
        Fetch all existing departments using a generator.

        :yield: A tuple containing department information.
        """

        query = "select * from departments"
        try:
            cur = self.con.cursor()
            cur.execute(query)
            for row in cur:
                yield row
        except Exception as e:
            logger.error(f"Error fetching departments: {e}")
            raise

    def fetch_department_using_dept_no(self, dept_no: str):
        """
        Fetch a department by department number.

        :param dept_no: The department number to search for.
        :yield: A tuple containing department information.
        """

        query = "select * from departments where dept_no = %s"
        try:
            cur = self.con.cursor()
            cur.execute(query, (dept_no,))
            for row in cur:
                yield row
        except Exception as e:
            logger.error(f"Error fetching department by dept_no: {e}")


if __name__ == "__main__":
    helper = DBHelper()

    for value in helper.fetch_all_departments():
        print(value)

    print()

    for value in helper.fetch_department_using_dept_no("d008"):
        print("Department number:", value[0])
        print("Department name:", value[1])
        print()
