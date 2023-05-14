
?crop=corn
<>
url('/v1/get_farm/<crop>/<season>', get_=farm)

@get('/v1/get_farm/<crop>')
def get_farm(request, crop, season):
    plo = request.quer
    #farm_list = []
    #valiate crop
    import awss3

    conn = awsds3.connetct('uarl')
    conn.download('bucket', filename)

    sssh auya@ksjhd
    /home/.ssh -> auth_key



    farm_list = [rec['farm'] for rec in data if crop == rec['crop']]
    #farm_list = lambda crop: for rec in data
    # for rec in data:
    #     if crop == rec['crop']:
    #         farm_list.append(rec['farm'])

    return farm_list


data = [

    {

        "farm": "farm1",

        "crop": "corn"

    },

    {

        "farm": "farm2",

        "crop": "soybean"

    },

    {

        "farm": "farm3",

        "crop": "corn"

    },

    {

        "farm": "farm4",

        "crop": "corn"

    },

    {

        "farm": "farm1",

        "crop": "rice"

    }

]


print(get_farm('rice'))
