from .log_manager import LogManager
from .trading_result import TradingResult
from .trading_request import TradingRequest

class VirtualMarket():
    '''
    거래 요청 정보를 받아서 처리하여 가상의 거래 결과 정보를 생성한다

    id: 요청 정보 id "1607862457.560075" request_id로 저장됨
    type: 거래 유형 sell, buy
    price: 거래 가격
    amount: 거래 수량
    '''

    def __init__(self):
        self.logger = LogManager.get_logger(__name__)

    def handle_request(self, request):
        return TradingResult(request.id, request.type, None, None)