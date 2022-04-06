BASE_URL = 'https://api.nftgo.io/api/v1/'
TOP_COLLECTION_PATH = 'ranking/collections?offset=0&limit=10&by=marketCap&interval=24h&asc=-1&rarity=-1&fields=marketCap,marketCapChange24h,relMarketCap,buyerNum24h,buyerNum24hChange24h,sellerNum24h,sellerNum24hChange24h,liquidity24h,liquidity24hChange24h,saleNum24h,saleNum24hChange24h,volume24h,relVolume24h,traderNum24h,traderNum24hChange24h,holderNum,holderNumChange24h,whaleNum,whaleNumChange24h,orderAvgPriceETH24h,orderAvgPriceETH24hChange24h,orderAvgPrice24h,orderAvgPrice24hChange24h,floorPrice,floorPriceChange24h'

USER_DATA_PATH = 'collection-new/data/'
MARKETCAP_VOLUME_REQUEST_PATH = '/chart/marketcap-volume-V2?cid='
PRICE_REQUEST_PATH = '/chart/price-V2?cid='
RANGE = '&range=30d'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}