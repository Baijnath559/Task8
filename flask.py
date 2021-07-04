from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

plates = [
    
{ "Number": "JH05AM7544","Description": "MARUTI WAGON R VXI (K-SERIES 1.0)", "RegistrationYear": "2012", "CarMake": { "CurrentTextValue": "MARUTI" }, "CarModel": { "CurrentTextValue": "WAGON R" }, "Variant": "VXI (K-SERIES 1.0)", "EngineSize": { "CurrentTextValue": "998" }, "MakeDescription": { "CurrentTextValue": "MARUTI" }, "ModelDescription": { "CurrentTextValue": "WAGON R" }, "NumberOfSeats": { "CurrentTextValue": "5" }, "VechileIdentificationNumber": "MA3EWDE1S00381944", "EngineNumber": "K10BN1506897", "FuelType": { "CurrentTextValue": "Petrol" }, "RegistrationDate": "21/02/2012", "Owner": "AMAN TIWARI", "Location": "DTO,EAST SINGHBHUM,JAMSHEDPUR", }
,
{ "Number": "JH01R1869","Description": "HYUNDAI SANTRO XING XK", "RegistrationYear": "2006", "CarMake": { "CurrentTextValue": "HYUNDAI" }, "CarModel": { "CurrentTextValue": "SANTRO XING XK" }, "Variant": "ERLX XK Non AC Petrol 1086.0", "EngineSize": { "CurrentTextValue": "1086.0" }, "MakeDescription": { "CurrentTextValue": "HYUNDAI" }, "ModelDescription": { "CurrentTextValue": "SANTRO XING XK" }, "NumberOfSeats": { "CurrentTextValue": "5" }, "VechileIdentificationNumber": "MALAA51HR6M001747L", "EngineNumber": "G4HG6M002245", "FuelType": { "CurrentTextValue": "PETROL" }, "RegistrationDate": "26/12/2006", "Owner": "GULZAR MANSURI", "Location": "DTO,RANCHI", }
,
{ "Number": "MH08AT3000","Description": "ROYAL ENFIELD THUNDER BIRD 350", "RegistrationYear": "2018", "CarMake": { "CurrentTextValue": "ROYAL ENFIELD" }, "CarModel": { "CurrentTextValue": "THUNDER BIRD" }, "Variant": "350", "EngineSize": { "CurrentTextValue": "350" }, "MakeDescription": { "CurrentTextValue": "ROYAL ENFIELD" }, "ModelDescription": { "CurrentTextValue": "THUNDER BIRD" }, "NumberOfSeats": { "CurrentTextValue": "2" }, "VechileIdentificationNumber": "ME3U3S5C1JL388398", "EngineNumber": "U3S5C1JL865351", "FuelType": { "CurrentTextValue": "Petrol" }, "RegistrationDate": "16/11/2018", "Owner": "ASHOK KUMAR", "Location": "DY.RTO,RATNAGIRI" }
, 
{ "Number": "MH20DV2366","Description": "SKODA SUPERB 2.0 TDI L&K AUTOMATIC TRANSMISSION", "RegistrationYear": "2016", "CarMake": { "CurrentTextValue": "SKODA" }, "CarModel": { "CurrentTextValue": "SUPERB" }, "EngineSize": { "CurrentTextValue": "1968" }, "MakeDescription": { "CurrentTextValue": "SKODA" }, "ModelDescription": { "CurrentTextValue": "SUPERB" }, "VechileIdentificationNumber": "TMBBKJNP6FA310011", "NumberOfSeats": { "CurrentTextValue": "5" }, "Colour": "", "EngineNumber": "CRG000518", "FuelType": { "CurrentTextValue": "Diesel" }, "RegistrationDate": "24-FEB-16","Owner": "CHARANJEET SINGH", "Location": "RTO,AURANGABAD"}

]



@app.route('/')
def index():
    return render_template('page.html')


@app.route('/app/api/plates/all')
def show():
    return jsonify(plates)


@app.route('/app/api/plates', methods = ['GET'])
def num():
    if 'Number' in request.args:
        num = request.args['Number']
    else:
        return "unknown request"
    
    result = []

    for plate in plates:
        if plate['Number'] == num:
            result.append(plate)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
