from bs4 import BeautifulSoup
from requests import get
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

FORMAT = "[%(levelname)s]: %(asctime)s %(name)s %(lineno)d [%(funcName)s] %(message)s"
formatter = logging.Formatter(FORMAT)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


url = "https://medium.com/@4yub1k/free-deploy-django-project-to-pythonanywhere-1f3f08a6447f"
ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"


class Medium:
    def __init__(self, url, ua) -> None:
        self.url = url
        try:
            if not isinstance(self.url, str):
                raise TypeError("Please provide URL string.")
            elif not self.url:
                raise ValueError("Please provide URL, it is empty!.")

            logger.info(f"Get url: {self.url}")
            with get(self.url, headers={"user-agent": ua}) as resp:
                # self.resp = resp.content
                self.headings_id_dict = self.getHeadings(resp.content)
        except TypeError as typeE:
            logger.exception(typeE)
        except ValueError as valueE:
            logger.exception(valueE)

    def getHeadings(self, html_content):
        logger.info("Getting page source (HTML).")
        try:
            soup = BeautifulSoup(html_content, "html.parser")
            headings = soup.find_all("h2", id=True)
            # print(headings)
            heading_id = [
                {"sub_head": heading.text, "href": f'#{heading["id"]}'}
                for heading in headings
            ]
            return heading_id
        except AttributeError as e:
            logger.exception(e)

    def htmlGenerate(self):
        # print(self.headings_id_dict)
        logger.info("Generating HTML..")
        return [
            f"<a href={self.url}{head['href']}'>{head['sub_head']}</a>"
            for head in self.headings_id_dict
        ]

    def plainPrint(self):
        logger.info("Printing Heading with href:")
        return "\n".join(
            [f"{head['sub_head']} {head['href']}" for head in self.headings_id_dict]
        )

    def listOrder(self, tag="", mark=""):
        return [
            f"<{tag}>{mark}<a href={self.url}{head['href']}'>{head['sub_head']}</a></{tag}>"
            for head in self.headings_id_dict
        ]

    def formattedHtml(self, mark="", type_order="ul"):
        logger.info("Formatting HTML...")
        if mark:
            return " ".join(self.listOrder(tag="p", mark=f"{mark}&nbsp;&nbsp;"))
            # return " ".join([f"<p>{mark}&nbsp;&nbsp;<a href={url}{head['href']}>{head['sub_head']}</a></p>" for head in self.headings_id_dict])
        return f'<{type_order}>{" ".join(self.listOrder(tag="li"))}</{type_order}>'


if __name__ == "__main__":
    med = Medium(url, ua)
    print(med.htmlGenerate())
    print(med.plainPrint())
    print(med.formattedHtml(mark="", type_order="ul"))
