import logging

def main():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(levelname)s %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",  
                        filename="logs.log")

    logging.debug("This is a DEBUG message")
    logging.info("This is an INFO message")
    logging.warning("This is a WARNING message")
    logging.error("This is an ERROR message")
    logging.critical("This is a CRITICAL message")

if __name__ == "__main__":
    main()
