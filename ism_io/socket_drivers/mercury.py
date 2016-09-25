# Driver class for Mercury Remote Control Outlets
# Codes are currently base on the 350.115UK sockets
# See https://www.amazon.co.uk/Mercury-350-115-Remote-Control-Adaptor-Black/dp/B0051NIJA4
from ism_io.socket_drivers.ooksocket import OokSocket


class Mercury(OokSocket):
    SOCKET_CODES = {
        1: {
            'on': '00000001000011100100001110010000100001000011100100001000010000111001000011100100001110010000100001110011100100001000011100111001',
            'off': '00000001000011100100001110010000100001000011100100001000010000111001000011100100001110010000100001110011100111001110010000100001'},
        2: {
            'on': '00000001000011100100001110010000100001000011100100001000010000111001000011100100001110011100111001000010000100001000011100111001',
            'off': '00000001000011100100001110010000100001000011100100001000010000111001000011100100001110011100111001000010000111001110010000100001'},
        3: {
            'on': '00000001000011100100001110010000100001000011100100001000010000111001000011100111001110010000100001000010000100001000011100111001',
            'off': '00000001000011100100001110010000100001000011100100001000010000111001000011100111001110010000100001000010000111001110010000100001'},
        4: {
            'on': '00000001000011100100001110010000100001000011100100001000010000111001110011100100001110010000100001000010000100001000011100111001',
            'off': '00000001000011100100001110010000100001000011100100001000010000111001110011100100001110010000100001000010000111001110010000100001'},
        5: {
            'on': '00000001000011100100001110010000100001000011100100001000011100111001000011100100001110010000100001000010000100001000011100111001',
            'off': '00000001000011100100001110010000100001000011100100001000011100111001000011100100001110010000100001000010000111001110010000100001'}
    }

    SYMBOL_DURATION = 0.00009
    TRANSMIT_ATTEMPTS = 15  # a sensible number of retries
    ATTEMPT_DELAY = 0.009  # the remote seems to use a similar delay

    def __init__(self, bit_driver, socket_id):
        OokSocket.__init__(self, bit_driver, socket_id)
