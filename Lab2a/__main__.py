import argparse
from modules import common
import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger()
parser = argparse.ArgumentParser(description='Приклад передачі аргументів у Python програму.')
parser.add_argument('-o', '--optional', dest='opt', type=str, help='Цей параметр є вибірковим.')
parser.add_argument('-l', '--logs', dest='logs', action='store_true',
                    help='Якщо виконати команду з цим параметром будуть виводитись логи.')
parser.add_argument('-pn', '--print-not', dest='pn', action='store_true', help='Друкує непарні числа')
parser.add_argument('-pe', '--print-even', dest='pe', action='store_true', help='Друкує парні числа')
parser.add_argument('-pr', '--print-error', dest='pr', action='store_true', help='')


def main(text):
    print(f"We are in the {__name__}")
    print(common.get_current_date().now())
    print(common.get_current_platform())
    if text:
        print("З консолі було передано аргумент\n", 10*"=", f">> {text} <<", 10*"=")


def how_to_write_logs():
    logger.info("Тут буде просто інформативне повідомлення")
    logger.warning("Це Warning повідомлення")
    logger.error("Це повідомлення про помилку")

def func_er(var1):
    c = 0
    c1 =  var1
    try:
        print("Що буде якщо c>c1", c>c1, "?")
    except Exception as e:
        logger.error("Це повідомлення про помилку")
        print(e)
    else:
        logger.info("Тут буде просто інформативне повідомлення")
    finally:
        print("А вот воно що!")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.logs:
        how_to_write_logs()
    else:
        main(args.opt)
    if args.pe:
        common.rangenum(1)
    if args.pn:
        common.rangenum(0)
    if args.pr:
        func_er('8')
