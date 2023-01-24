import requests


class Skud(requests.Session):
    def __init__(self, link: str, sn: int) -> None:
        super(Skud, self).__init__()
        self.sn = sn
        self.link = link

        self.headers.update(
            {'content-type': 'application/json', 'accept': 'application/json', 'user-agent': 'Z5R WEB', })

    def request(self, method, url=None, params=None, data=None, headers=None, cookies=None, files=None, auth=None,
                timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None,
                json=None):
        question = {'sn': self.sn, 'type': 'Z5RWEB'}
        question.update({'messages': json})
        url = self.link
        return super(Skud, self).request(method, url, params=None, data=None, headers=None, cookies=None, files=None,
                                         auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None,
                                         stream=None, verify=None, cert=None, json=question)
