import json
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        url = "https://www.walmart.com/search?q=ipads"
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        script_tag = response.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
        if script_tag:
            json_data = json.loads(script_tag)  # Convert string to Python dict
            print(json_data["props"]["pageProps"]["initialData"].keys())
            yield json_data  # Yield the extracted JSON to store in output file
