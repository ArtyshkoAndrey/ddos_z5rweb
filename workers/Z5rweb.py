import threading
import time

from requests import Response
import datetime

from .Skud import Skud


class Z5rweb(threading.Thread):
    # Инициализация
    def __init__(self, link: str, sn: int) -> None:
        super(Z5rweb, self).__init__(daemon=True)
        self.link = link
        self.sn = sn
        self.session = Skud(link=self.link, sn=self.sn)

    def run(self) -> None:
        now = datetime.datetime.now()
        response = self.power_on()
        counter = 0
        while True:
            answer = self.get_success(response)
            if counter % 4 == 0:
                answer.append({
                    "id": 123456789,
                    "operation": "events",
                    "events": [
                        {
                            "event": 0,
                            "card": "000000000000",
                            "time": now.strftime("%Y-%m-%d %H:%M:%S"),
                        }
                    ]
                })

            if counter % 3 == 0:
                answer.append({
                    "id": 123456789,
                    "operation": "events",
                    "events": [
                        {
                            "event": 4,
                            "card": "00B5009EC1A8",
                            "time": now.strftime("%Y-%m-%d %H:%M:%S"),
                            "flag": 0
                        }
                    ]
                })
            response = self.session.post('/', json=answer)
            counter += 1
            # time.sleep(2)

    def power_on(self) -> Response:
        response = self.session.post(url='/', json=[
            {
                "id": 123456789,
                "operation": "power_on",
                "fw": "1.0.1",
                "conn_fw": "2.0.2",
                "active": 0,
                "mode": 0,
                "controller_ip": "95.188.80.41"
            }
        ])
        if response.status_code != 200:
            time.sleep(10)
            return self.power_on()
        return response

    def get_success(self, response: Response) -> list:
        messages = response.json().get('messages')
        answer = list()
        for item in messages:
            print(item)
            answer.append({
                'success': 1,
                'id': item.get('id')
            })

        answer.append({
            "id": 123456789,
            "operation": "ping",
            "active": 1,
            "mode": 0
        })
        return answer
