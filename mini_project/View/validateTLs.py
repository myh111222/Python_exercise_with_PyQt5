TEST_DATA = {
    'roads': [
        { 'id': 'road-1' },
        { 'id': 'road-2' }
    ],
    'trafficLights': [
        {
            'id': 'tl-1',
            'bulbs': [
                { 'id': 'tlb-1', 'shape': 'circle' },
                { 'id': 'tlb-1', 'shape': 'arrow', 'toRoad': 'road-2' }
            ]
        },
        {
            'id': 'tl-2',
            'bulbs': [
                { 'id': 'tlb-2', 'shape': 'circle', 'toRoad': 'road-1' }
            ]
        },
        {
            'id': 'tl-3',
            'bulbs': [
                { 'id': 'tlb-3', 'shape': 'arrow' }
            ]
        },
        {
            'id': 'tl-4',
            'bulbs': [
                { 'id': 'tlb-4', 'shape': 'arrow', 'toRoad': 'xyz' }
            ]
        }
    ]
}



def validate_traffic_lights(data):
    results=[]
    roadlist=[]
    #print (data['trafficLights'][0]['bulbs'][0]['shape']        )
#    for road in data['roads']:
#        print (road['id'])
#        roadlist.append(road['id'])

    roadlist=[road['id'] for road in data['roads']]
    
    print (roadlist)
    for i in data['trafficLights']:
        for j in i['bulbs']:
               # print (data['roads'])
            pass
            #print (j['shape'])
            if ( j['shape']=='circle' and ( ('toRoad' in j))):
                print (j['id'])
                results.append(j['id'])
            elif ((j['shape']=='arrow' and   ('toRoad' not in j) )):
                print (j['id'])
                results.append(j['id'])
            elif ((j['shape']=='arrow' and   (j['toRoad'] not in roadlist) )):
                print (j['id'])
                results.append(j['id'])

        #print (data['trafficLights'][0]['bulbs'][0]['shape'])



    '''
    Returns list of TL ids that fail these conditions:
    1. if TL bulb shape is 'circle', toRoad must not be set
    2. if TL bulb shape is 'arrow', toRoad is required
    3. if TL bulb shape is 'arrow', toRoad must be a valid road id
    '''
    return results


if __name__ == '__main__':
    results = validate_traffic_lights(TEST_DATA)
    # assert(results == ['tl-2', 'tl-3', 'tl-4'])
    print(results)
