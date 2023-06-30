import json
import os

from PIL import Image, ImageChops
from playwright.sync_api import Route

secret_phrase = 'endorse boat cream purpose north toddler panda frame ecology way smile success'
password = 'Versus007//'
wallet = '0xd5ed26d93129a8b51ac54b40477327f6511824b6'


def keys_data():
    base_dir = os.getenv('GITHUB_WORKSPACE', '/Users/annaskvortsova/PycharmProjects/UiTests')
    file_path = os.path.join(base_dir, 'keys.json')
    dictionary = open(file_path).read()
    nets = json.loads(dictionary)
    return nets


def screenshot_comparison(base_image: str, test_image: str):
    reference_image = Image.open(base_image).convert('RGB')
    screenshot_image = Image.open(test_image).convert('RGB')
    diff_image = ImageChops.difference(reference_image, screenshot_image)
    diff_image.show()
    diff_image.save("diff_image.png")
    assert diff_image.getbbox() is None, "Изображения различаются. Различия сохранены в файле diff_image.png."


def intercept_request(route, request):
    print(request.url)
    print(request.method)
    print(request.headers)
    print(request.post_data)
    # Продолжить запрос
    route.continue_()


# ---------------------------------------------------------------------------------------------
mock_body = {
    "eth": '{"ok":true,"data":{"eth_trx":{"amount":"6.356719","price":{"BTC":"0.00000244","USD":"0.070583"}},"eth_cusdt":{"amount":"4.53186625","price":{"BTC":"0.000000556884","USD":"0.01616398"}},"eth_usdt":{"amount":"1.259487","price":{"BTC":"0.00003457","USD":"1.001"}},"eth_sand":{"amount":"0.2928876096037162","price":{"BTC":"0.00001401","USD":"0.405216"}},"eth_zrx":{"amount":"0.29057215621818195","price":{"BTC":"0.00000641","USD":"0.185415"}},"eth_ceth":{"amount":"0.25402822","price":{"BTC":"0.00126172","USD":"36.5"}},"eth_1inch":{"amount":"0.19674526862879117","price":{"BTC":"0.00001027","USD":"0.297169"}},"eth_weth":{"amount":"0.19041916808356166","price":{"BTC":"0.06280536","USD":"1816.06"}},"eth_uni":{"amount":"0.07850502918345027","price":{"BTC":"0.00015669","USD":"4.53"}},"eth_aave":{"amount":"0.0221507783976732","price":{"BTC":"0.00184144","USD":"53.24"}},"eth_dia":{"amount":"0.02001929367279853","price":{"BTC":"0.00000827","USD":"0.239218"}},"eth_dydx":{"amount":"0.006577627362976092","price":{"BTC":"0.00006135","USD":"1.77"}},"eth_usdc":{"amount":"0.003084","price":{"BTC":"0.00003456","USD":"0.999441"}},"eth_tusd":{"amount":"0.001586786113770929","price":{"BTC":"0.00003452","USD":"0.998483"}},"eth_dai":{"amount":"0.001551127290260995","price":{"BTC":"0.00003454","USD":"1"}},"eth_steth":{"amount":"0.001006056876755921","price":{"BTC":"0.06291601","USD":"1828.17"}},"eth_wbtc":{"amount":"0.00007176","price":{"BTC":"0.99996649","USD":"28915"}},"eth_comp":{"amount":"0.000018365953384395","price":{"BTC":"0.00099843","USD":"28.88"}}},"error":""}',
    "bsc": '{"ok":true,"data":{"bsc_oleg":{"amount":90000,"price":{"BTC":0,"USD":0}},"bsc_xct":{"amount":316.587844,"price":{"BTC":"0.000000185981","USD":"0.00538601"}},"bsc_trx":{"amount":10.867071133158767,"price":{"BTC":"0.00000244","USD":"0.070583"}},"bsc_alpaca":{"amount":1.877389856701773,"price":{"BTC":"0.00000507","USD":"0.146681"}},"bsc_bsw":{"amount":1.7374916769482223,"price":{"BTC":"0.00000299","USD":"0.086452"}},"bsc_cake":{"amount":0.29360837493410324,"price":{"BTC":"0.00004847","USD":"1.4"}},"bsc_busd-t":{"amount":0.1277130439239808,"price":{"BTC":"0.00003457","USD":"1.001"}},"bsc_usdc":{"amount":0.09851108981841084,"price":{"BTC":"0.00003456","USD":"0.999441"}},"bsc_atom":{"amount":0.02833293554459173,"price":{"BTC":"0.00030395","USD":"8.79"}},"bsc_busd":{"amount":0.025625205824344105,"price":{"BTC":"0.00003451","USD":"0.998124"}},"bsc_1inch":{"amount":0.005592662787849809,"price":{"BTC":"0.00001027","USD":"0.297169"}},"bsc_wbnb":{"amount":0.002588353261844987,"price":{"BTC":"0.00849508","USD":"245.73"}},"bsc_eth":{"amount":0.000015620694287116,"price":{"BTC":"0.06283199","USD":"1819.74"}}},"error":""}',
    "polygon": '{"ok":true,"data":{"polygon_usdt":{"amount":"0.30581","price":{"BTC":"0.00003457","USD":"1.001"}},"polygon_1inch":{"amount":"0.211335736639124114","price":{"BTC":"0.00001027","USD":"0.297169"}},"polygon_usdc":{"amount":"0.111562","price":{"BTC":"0.00003456","USD":"0.999441"}},"polygon_arpa":{"amount":"0.026518392334422163","price":{"BTC":0,"USD":0}},"polygon_aave":{"amount":"0.022773713609935732","price":{"BTC":"0.00184144","USD":"53.24"}},"polygon_weth":{"amount":"0.000466381778832643","price":{"BTC":"0.06280536","USD":"1816.06"}}},"error":""}',
    "arbitrum": '{"ok":true,"data":{"arbitrum_usdt":{"amount":"7.438303","price":{"BTC":"0.00003457","USD":"1.001"}},"arbitrum_sushi":{"amount":"2.160711475728064931","price":{"BTC":"0.00002145","USD":"0.6205"}},"arbitrum_usdc":{"amount":"0.999631","price":{"BTC":"0.00003456","USD":"0.999441"}},"arbitrum_arb":{"amount":"0.822096389511406463","price":{"BTC":"0.0000000072046707","USD":"0.00020362009"}},"arbitrum_usdc.e":{"amount":"0.331993","price":{"BTC":0,"USD":0}}},"error":""}',
    "avalanche": '{"ok":true,"data":{"avalanche_usdt":{"amount":"0.051634","price":{"BTC":"0.00003442","USD":"1.001"}}},"error":""}',
    "optimism": '{"ok":true,"data":{"optimism_usdt":{"amount":"10.874371","price":{"BTC":"0.00003457","USD":"1.001"}},"optimism_aave":{"amount":"0.085425255637175817","price":{"BTC":"0.00184144","USD":"53.24"}},"optimism_usdc":{"amount":"0.055435","price":{"BTC":"0.00003456","USD":"0.999441"}},"optimism_bond":{"amount":"0.027369063844709634","price":{"BTC":"0.00009976","USD":"2.88"}}},"error":""}'}


def handle_route_balance(route: Route) -> None:
    # Fetch original response.
    response = route.fetch()
    # Add a prefix to the title.
    old_body = response.text()
    print(old_body)
    mock_body = '{"ok":true,"data":{"mainBalance":999,"delegatedBalance":0,"originatedAddresses":[],"adding":[],' \
                '"stake":0,"frozenBalance":0,"frozen":[],"unstake":0},"error":""}'
    route.fulfill(
        # Pass all fields from the response.
        response=response,
        # Override response body.
        body=mock_body,
        # Force content type to be html.
        headers={**response.headers, "content-type": "application/json; charset=utf-8"},
    )


def handle_route_tokens_version_by_eth(route: Route) -> None:
    mock_body = '{"ok":true,"data":{"eth_trx":{"amount":"6.356719","price":{"BTC":"0.00000244","USD":"0.070583"}},"eth_cusdt":{"amount":"4.53186625","price":{"BTC":"0.000000556884","USD":"0.01616398"}},"eth_usdt":{"amount":"1.259487","price":{"BTC":"0.00003457","USD":"1.001"}},"eth_sand":{"amount":"0.2928876096037162","price":{"BTC":"0.00001401","USD":"0.405216"}},"eth_zrx":{"amount":"0.29057215621818195","price":{"BTC":"0.00000641","USD":"0.185415"}},"eth_ceth":{"amount":"0.25402822","price":{"BTC":"0.00126172","USD":"36.5"}},"eth_1inch":{"amount":"0.19674526862879117","price":{"BTC":"0.00001027","USD":"0.297169"}},"eth_weth":{"amount":"0.19041916808356166","price":{"BTC":"0.06280536","USD":"1816.06"}},"eth_uni":{"amount":"0.07850502918345027","price":{"BTC":"0.00015669","USD":"4.53"}},"eth_aave":{"amount":"0.0221507783976732","price":{"BTC":"0.00184144","USD":"53.24"}},"eth_dia":{"amount":"0.02001929367279853","price":{"BTC":"0.00000827","USD":"0.239218"}},"eth_dydx":{"amount":"0.006577627362976092","price":{"BTC":"0.00006135","USD":"1.77"}},"eth_usdc":{"amount":"0.003084","price":{"BTC":"0.00003456","USD":"0.999441"}},"eth_tusd":{"amount":"0.001586786113770929","price":{"BTC":"0.00003452","USD":"0.998483"}},"eth_dai":{"amount":"0.001551127290260995","price":{"BTC":"0.00003454","USD":"1"}},"eth_steth":{"amount":"0.001006056876755921","price":{"BTC":"0.06291601","USD":"1828.17"}},"eth_wbtc":{"amount":"0.00007176","price":{"BTC":"0.99996649","USD":"28915"}},"eth_comp":{"amount":"0.000018365953384395","price":{"BTC":"0.00099843","USD":"28.88"}}},"error":""}'
    # Fetch original response.
    response = route.fetch()
    # Add a prefix to the title.
    old_body = response.text()
    print(old_body)
    # mock_body = '{"ok":true,"data":{"avalanche_usdt":{"amount":"0.051634","price":{"BTC":"0.00003442","USD":"1.001"}}},"error":""}'
    route.fulfill(
        # Pass all fields from the response.
        response=response,
        # Override response body.
        body=mock_body,
        # Force content type to be html.
        headers={**response.headers, "content-type": "application/json; charset=utf-8"},
    )


def handle_route_tokens_version_by_bsc(route: Route) -> None:
    mock_body = '{"ok":true,"data":{"bsc_oleg":{"amount":77700,"price":{"BTC":0,"USD":0}},"bsc_xct":{"amount":316.587844,"price":{"BTC":"0.000000185981","USD":"0.00538601"}},"bsc_trx":{"amount":10.867071133158767,"price":{"BTC":"0.00000244","USD":"0.070583"}},"bsc_alpaca":{"amount":1.877389856701773,"price":{"BTC":"0.00000507","USD":"0.146681"}},"bsc_bsw":{"amount":1.7374916769482223,"price":{"BTC":"0.00000299","USD":"0.086452"}},"bsc_cake":{"amount":0.29360837493410324,"price":{"BTC":"0.00004847","USD":"1.4"}},"bsc_busd-t":{"amount":0.1277130439239808,"price":{"BTC":"0.00003457","USD":"1.001"}},"bsc_usdc":{"amount":0.09851108981841084,"price":{"BTC":"0.00003456","USD":"0.999441"}},"bsc_atom":{"amount":0.02833293554459173,"price":{"BTC":"0.00030395","USD":"8.79"}},"bsc_busd":{"amount":0.025625205824344105,"price":{"BTC":"0.00003451","USD":"0.998124"}},"bsc_1inch":{"amount":0.005592662787849809,"price":{"BTC":"0.00001027","USD":"0.297169"}},"bsc_wbnb":{"amount":0.002588353261844987,"price":{"BTC":"0.00849508","USD":"245.73"}},"bsc_eth":{"amount":0.000015620694287116,"price":{"BTC":"0.06283199","USD":"1819.74"}}},"error":""}'
    response = route.fetch()
    old_body = response.text()
    print(old_body)
    route.fulfill(
        response=response,
        body=mock_body,
        headers={**response.headers, "content-type": "application/json; charset=utf-8"},
    )


def handle_route_tokens_version_by_polygon(route: Route) -> None:
    mock_body = '{"ok":true,"data":{"polygon_usdt":{"amount":"0.30581","price":{"BTC":"0.00003457","USD":"1.001"}},"polygon_1inch":{"amount":"0.211335736639124114","price":{"BTC":"0.00001027","USD":"0.297169"}},"polygon_usdc":{"amount":"0.111562","price":{"BTC":"0.00003456","USD":"0.999441"}},"polygon_arpa":{"amount":"0.026518392334422163","price":{"BTC":0,"USD":0}},"polygon_aave":{"amount":"0.022773713609935732","price":{"BTC":"0.00184144","USD":"53.24"}},"polygon_weth":{"amount":"0.000466381778832643","price":{"BTC":"0.06280536","USD":"1816.06"}}},"error":""}'
    # Fetch original response.
    response = route.fetch()
    # Add a prefix to the title.
    old_body = response.text()
    # mock_body = '{"ok":true,"data":{"avalanche_usdt":{"amount":"0.051634","price":{"BTC":"0.00003442","USD":"1.001"}}},"error":""}'
    route.fulfill(
        # Pass all fields from the response.
        response=response,
        # Override response body.
        body=mock_body,
        # Force content type to be html.
        headers={**response.headers, "content-type": "application/json; charset=utf-8"},
    )


def handle_route_tokens_version_by_arbitrum(route: Route) -> None:
    mock_body = '{"ok":true,"data":{"arbitrum_usdt":{"amount":"7.654321","price":{"BTC":"0.00003457","USD":"1.001"}},"arbitrum_sushi":{"amount":"2.160711475728064931","price":{"BTC":"0.00002145","USD":"0.6205"}},"arbitrum_usdc":{"amount":"0.999631","price":{"BTC":"0.00003456","USD":"0.999441"}},"arbitrum_arb":{"amount":"0.822096389511406463","price":{"BTC":"0.0000000072046707","USD":"0.00020362009"}},"arbitrum_usdc.e":{"amount":"0.331993","price":{"BTC":0,"USD":0}}},"error":""}'
    # Fetch original response.
    response = route.fetch()
    # Add a prefix to the title.
    old_body = response.text()
    print(old_body)
    # mock_body = '{"ok":true,"data":{"avalanche_usdt":{"amount":"0.051634","price":{"BTC":"0.00003442","USD":"1.001"}}},"error":""}'
    route.fulfill(
        # Pass all fields from the response.
        response=response,
        # Override response body.
        body=mock_body,
        # Force content type to be html.
        headers={**response.headers, "content-type": "application/json; charset=utf-8"},
    )


def handle_route_tokens_version_by_avalanche(route: Route) -> None:
    mock_body = '{"ok":true,"data":{"avalanche_usdt":{"amount":"0.051634","price":{"BTC":"0.00003442","USD":"1.001"}}},"error":""}'
    # Fetch original response.
    response = route.fetch()
    # Add a prefix to the title.
    old_body = response.text()
    print(old_body)
    # mock_body = '{"ok":true,"data":{"avalanche_usdt":{"amount":"0.051634","price":{"BTC":"0.00003442","USD":"1.001"}}},"error":""}'
    route.fulfill(
        # Pass all fields from the response.
        response=response,
        # Override response body.
        body=mock_body,
        # Force content type to be html.
        headers={**response.headers, "content-type": "application/json; charset=utf-8"},
    )


def handle_route_tokens_version_by_optimism(route: Route) -> None:
    mock_body = '{"ok":true,"data":{"optimism_usdt":{"amount":"10.874371","price":{"BTC":"0.00003457","USD":"1.001"}},"optimism_aave":{"amount":"0.085425255637175817","price":{"BTC":"0.00184144","USD":"53.24"}},"optimism_usdc":{"amount":"0.055435","price":{"BTC":"0.00003456","USD":"0.999441"}},"optimism_bond":{"amount":"0.027369063844709634","price":{"BTC":"0.00009976","USD":"2.88"}}},"error":""}'
    response = route.fetch()
    old_body = response.text()
    print(old_body)
    # mock_body = '{"ok":true,"data":{"avalanche_usdt":{"amount":"0.051634","price":{"BTC":"0.00003442","USD":"1.001"}}},"error":""}'
    route.fulfill(
        response=response,
        body=mock_body,
        headers={**response.headers, "content-type": "application/json; charset=utf-8"},
    )
