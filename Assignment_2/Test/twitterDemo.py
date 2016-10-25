import twitter

api = twitter.Api(consumer_key='Gfi9Gt4imoHDKNuhTqH0RvkJD',
                      consumer_secret='YU4ukWbn8ROr1JXph9HtiXCBWh96rY0LpedN5ny8t35pLvHcgd',
                      access_token_key='2865250744-BJcNzHyOeGcAyD8ImHyHItNPZS6Md4wXLMKyN4M',
                      access_token_secret='hZI8R5bZ4T7vlBw5ejQUv0ChabmqrmHcdteHC9csOfo1B')
api.PostUpdate(status = 'Posting to twitter from python. #python, #test')
print(api.VerifyCredentials())
