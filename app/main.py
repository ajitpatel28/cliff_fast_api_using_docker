from fastapi import FastAPI, Body, Depends
from elasticsearch import Elasticsearch
import uvicorn
from  model import UserSchema, UserLoginSchema
from auth_bearrer import JWTBearer
from auth_handller import signJWT

es = Elasticsearch('https://products104:Products104@@search-healthos-es67-nocrz73cfktuhhkgnaz72td3cq.us-east-1.es'
                    '.amazonaws.com')

users = []

app = FastAPI()


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# route handlers

# Welcome
@app.get("/", tags=["test"])
def greet():
    return {"hello": "Cliff!."}


# Get API responses
@app.get("/count_discounted_products", dependencies=[Depends(JWTBearer())], tags=["count_discounted_products"])
def get_count_discounted_products():
    for x in range(len(sources)):
        query = {
            "query": {

                "bool": {

                    "must_not": [{
                        "term": {"similar_products.website_results." + sources[x] + ".meta.avg_discount": 0}
                    }]
        }
        }
        }
    response = es.count(index="products104", body=query)

    return {"data": response}


@app.get("/count_products_by_brand", dependencies=[Depends(JWTBearer())], tags=["count_products_by_brand"])
def get_count_products_by_brand():
    data = []
    _count = []
    res = []
    for x in range(len(sources)):
        source = []
        source.append("similar_products.website_results." + sources[x] + ".knn_items._source.brand.name.keyword")
        for i in range(len(source)):
            query = {"size": 0,
                     "aggs": {
                         "brand": {
                             "terms": {
                                 "field": source[i]
                             }}
                     }
                     }
        response = es.search(index="products104", body=query)
        res.append(response)

    for i in res:
        for z in i:
            c = list(i.items())[4][1]['brand']['buckets']
        data.append(c)


    brand_with_product = {}
    brands = []
    prodcut_counts = []
    for i in data:

        for x in i:
            for z in x:
                v = x['key']
                c = x['doc_count']
            brands.append(v)
            prodcut_counts.append(c)

    for brand, prodcut_count in zip(brands, prodcut_counts):
        if brand in brand_with_product:
            brand_with_product[brand] += prodcut_count
        else:
            brand_with_product[brand] = prodcut_count

    return {"data": brand_with_product}


@app.get("/count_high_offer_price", dependencies=[Depends(JWTBearer())], tags=["count_high_offer_price"])
def get_count_products_by_brand():
    result = {}
    _count = []
    res = []
    d = []

    for x in range(len(sources)):
        source = []
        source.append("similar_products.website_results." + sources[x] + ".knn_items._source.price.offer_price.value")

        for i in range(len(source)):
            query = {"query": {
                "range": {
                    source[i]: {
                        "gte": 300
                    }
                }
            }}
            response = es.count(index="products104", body=query)
            res.append(response)
    for i in res:
        for z in i:
            c = list(i.items())[0]
            _count.append(c[1])
        d = i['_shards']

        Total_count = sum(_count)
        result.update({'_count': Total_count})
        result.update({'_shards': d})

    return {"data": result}


@app.get("/top_20_discounting_brands", dependencies=[Depends(JWTBearer())], tags=["top_20_discounting_brands"])
def get_count_products_by_brand():
    data_brand_name = []
    discount_price = []
    discount_source_data = []
    res = []
    res_discount = []
    brands = []
    brand_list = []
    final_brand_list = []
    for x in range(len(sources)):
        source_discount = []
        source_discount.append("similar_products.website_results." + sources[x] + ".meta.avg_discount")

        for i in range(len(source_discount)):
            query_discount = {

                "_source": source_discount[i]

            }
        response = es.search(index="products104", body=query_discount)

        res_discount.append(response)
    for i in res_discount:
        d = i['hits']['hits']
        discount_source_data.append(d)

    for i in discount_source_data:
        for z in i:
            try:
                a = z['_source']['similar_products']['website_results']
                x = next(iter(a))
                price = float(a[x]['meta']['avg_discount'])

                discount_price.append(price)

                query_brand_name = {"size": 0,
                                    "aggs": {
                                        "brand": {
                                            "terms": {
                                                "field": "similar_products.website_results." + str(
                                                    x) + ".knn_items._source.brand.name.keyword"
                                            }}
                                    }
                                    }
                response_brand_name = es.search(index="products104", body=query_brand_name)
                res.append(response_brand_name)
            except:
                pass

    for i in res:
        for z in i:
            c = list(i.items())[4][1]['brand']['buckets']
        data_brand_name.append(c)

    for i in data_brand_name:

        for x in i:
            for z in x:
                v = x['key']
                c = x['doc_count']
            brands.append(v)

    merged_list_brand_discount = list(tuple(zip(brands, discount_price)))
    merged_list_brand_discount.sort(key=lambda t: t[1], reverse=True)

    for x in merged_list_brand_discount:
        brand_list.append(x[0])
    brand_list = list(dict.fromkeys(brand_list))

    for x in brand_list[:20]:
        final_brand_list.append(x)
    return {"data": final_brand_list}


@app.get("/count_high_discount_products_by_brands", dependencies=[Depends(JWTBearer())],
         tags=["count_high_discount_products_by_brands"])
def get_count_products_by_brand():
    data = []
    data_discount_price = []
    data_source_discount = []
    res_brand = []
    res_source_discount = []
    brand_with_product_count = {}
    brands = []
    prodcut_counts = []

    for x in range(len(sources)):
        source_avg_discoount = []
        source_avg_discoount.append("similar_products.website_results." + sources[x] + ".meta.avg_discount")

        for i in range(len(source_avg_discoount)):
            query_source_discount = {
                "_source": source_avg_discoount[i]

            }
        response = es.search(index="products104", body=query_source_discount)

        res_source_discount.append(response)
    for i in res_source_discount:
        d = i['hits']['hits']
        data_source_discount.append(d)

    for i in data_source_discount:
        for z in i:
            a = z['_source']['similar_products']['website_results']
            x = next(iter(a))
            price = float(a[x]['meta']['avg_discount'])

            data_discount_price.append(price)

            flag = False
            if price > 0.25:
                flag = True
                query = {"size": 0,
                         "aggs": {
                             "brand": {
                                 "terms": {
                                     "field": "similar_products.website_results." + str(
                                         x) + ".knn_items._source.brand.name.keyword"
                                 }}
                         }
                         }
                response_brand = es.search(index="products104", body=query)
                res_brand.append(response_brand)
                if flag == True:
                    for i in res_brand:
                        for z in i:
                            c = list(i.items())[4][1]['brand']['buckets']
                        data.append(c)

                for i in data:
                    for x in i:
                        for z in x:
                            v = x['key']
                            c = x['doc_count']
                        brands.append(v)
                        prodcut_counts.append(c)

                for brand, prodcut_count in zip(brands, prodcut_counts):
                    if brand in brand_with_product_count:
                        brand_with_product_count[brand] += prodcut_count
                    else:
                        brand_with_product_count[brand] = prodcut_count


    return {"data": brand_with_product_count}


@app.get("/count_by_category_and_stock", dependencies=[Depends(JWTBearer())], tags=["count_by_category_and_stock"])
def get_count_products_by_brand():
    data = []
    _count = []
    res = []
    categories = []
    in_stock = {}
    out_stock = {}
    in_stock_count = []
    out_stock_count = []
    for x in range(len(sources)):
        source = []
        stock_source = []
        source.append("similar_products.website_results." + sources[x] + ".knn_items._source.classification.l1.keyword")
        stock_source.append("similar_products.website_results." + sources[x] + ".knn_items._source.stock.available")

        for i in range(len(source)):
            query = {

                "size": 0,
                "aggs": {
                    "category": {
                        "terms": {
                            "field": source[i]
                        },
                        "aggs": {
                            "stock": {
                                "terms": {
                                    "field": stock_source[i]
                                }
                            }
                        }
                    }
                }
            }

        response = es.search(index="products104", body=query)
        res.append(response)

    for i in res:
        for z in i:
            c = list(i.items())[4][1]['category']['buckets']
        data.append(c)

    for i in data:
        for x in i:
            l = x['key']
            categories.append(l)
            b = x['stock']['buckets']
            for z in b:

                if (z['key'] == 1):
                    s = list(z.items())[2][1]
                    in_stock_count.append(s)
                    for category, _in_stock in zip(categories, in_stock_count):
                        if category in in_stock:
                            in_stock[category] += _in_stock

                        else:
                            in_stock[category] = _in_stock



                elif (z['key'] == 0):
                    s = list(z.items())[2][1]
                    out_stock_count.append(s)
                    for category, _out_stock in zip(categories, out_stock_count):
                        if category in out_stock:
                            out_stock[category] += _out_stock

                        else:
                            out_stock[category] = _out_stock

    return {"In stock": in_stock, "Out of stock": out_stock}


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body(...)):
    users.append(user)  # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

# list of id's common in whole data of elasticsearch to traverse through whole data
sources = ["6188e422afaf2b4e847b340e",
           "6189061cb1438e7d97084227",
           "62037d06110b3f66c0238d5c",
           "61fa840764a7e4f3ca859a56",
           "62037c8c110b3f66c0238d5b",
           "62037a37110b3f66c0238d5a",
           "618a5fcb2324f3ad279b24dc"
           ]
