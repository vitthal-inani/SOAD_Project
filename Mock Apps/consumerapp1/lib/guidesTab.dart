import 'dart:convert';
import 'package:consumerapp1/Models/Guide.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'GuideFilter.dart';

import 'Models/City.dart';
import 'ServerCalls.dart';
import 'globals.dart';

class GuidesTab extends StatefulWidget {
  City cityModel;
  GuidesTab({this.cityModel});
  @override
  _GuidesTabState createState() => _GuidesTabState();
}

class _GuidesTabState extends State<GuidesTab> {
  DateTime _startDate;
  DateTime _endDate;
  bool isSet = false;


  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    // StripePayment.setOptions(
    //     StripeOptions(publishableKey: "pk_test_51Hs6R2DAfuv0xqE2CobhhssqYoz2lNgJw6Qs9jEhSMzM6QCOyUwS3Hx2U6wcVC8wZ5yuzjvSV3kpVZZSStyavwz700E5Brgvja", merchantId: "Test", androidPayMode: 'test'));
  }

  // var guide = Guide.fromJSON({
  //   "guide_name": "Chandler Bing",
  //   "guide_id": 2,
  //   "rating": 3.0,
  //   "monument_names": ["Monument A","Monument B"],
  //   "imageURL": "https://image.shutterstock.com/image-vector/young-man-face-cartoon-260nw-1224888760.jpg"
  // });

  _setSet(){
    print("hit");
    setState(() {
      isSet=true;
    });
  }



  _showPaymentDialog(Guide1 guide1){
    return showDialog<void>(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Book Guide : '+ guide1.name),
          content: Text('Pay in INR: '+ guide1.cost.toString()),
          actions: <Widget>[
            TextButton(
              child: Text('Create Source'),
              onPressed: () {

              },
            ),
            TextButton(
              child: Text('Continue Payment'),
              onPressed: () {
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    // final userModel=Provider.of<User>(context);
    // final cityModel=Provider.of<City>(context);
    return ChangeNotifierProvider(
      create: (_) => BookGuide(),
      child: Container(
        padding: EdgeInsets.all(20),
        child: Column(
          children: [
            //  guide filter
            GuideFilter(
              width: _screenSize.width,
              onDone: _setSet(),
            ),
            Padding(
              padding: EdgeInsets.all(_screenSize.height * 0.01),
            ),
            //  cards
            Consumer<BookGuide>(
              builder: (context, bookGuide, child){
                return Container(
                  width: _screenSize.width*0.85,
                  height: _screenSize.height * 0.65,
                  child: FutureBuilder(
                      future: DataService.getGuides(api_key),
                      builder: (context, snapshot) {
                        if(snapshot.connectionState==ConnectionState.done){
                          if(snapshot.hasData){
                            Response response=snapshot.data;
                            if(response.statusCode==200){
                              List json = jsonDecode(response.body);
                              print(json);
                              return ListView.separated(
                                shrinkWrap: true,
                                itemCount: json.length,
                                separatorBuilder: (context, idx) {
                                  return Padding(
                                    padding: EdgeInsets.all(8),
                                  );
                                },
                                itemBuilder: (context, idx) {
                                  Guide1 guide=Guide1.fromJSON(json[idx]);
                                  return InkWell(
                                    onTap: (){
                                      _showPaymentDialog(guide);
                                    },
                                    child: Card(
                                      elevation: 10,
                                      child: Container(
                                        height: _screenSize.height * 0.2,
                                        padding: EdgeInsets.all(10),
                                        child: Row(
                                          children: [
                                            Image.network(
                                              guide.imageURL,
                                              fit: BoxFit.fill,
                                              loadingBuilder: (BuildContext context, Widget child,
                                                  ImageChunkEvent loadingProgress) {
                                                if (loadingProgress == null) return child;
                                                return Center(
                                                  child: CircularProgressIndicator(
                                                    value: loadingProgress.expectedTotalBytes !=
                                                        null
                                                        ? loadingProgress.cumulativeBytesLoaded /
                                                        loadingProgress.expectedTotalBytes
                                                        : null,
                                                  ),
                                                );
                                              },
                                              height: _screenSize.height*0.2,
                                              width: _screenSize.width*0.2,
                                            ),
                                            Flexible(
                                              child: Container(
                                                padding: EdgeInsets.all(8),
                                                child: Column(
                                                  crossAxisAlignment: CrossAxisAlignment.start,
                                                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                                                  children: [
                                                    Flexible(
                                                        child: Text(
                                                          guide.name,
                                                          overflow: TextOverflow.ellipsis,
                                                          style: GoogleFonts.raleway(
                                                            fontSize: 20,
                                                          ),
                                                        )),
                                                    Flexible(
                                                        child: Text(
                                                          guide.username,
                                                          overflow: TextOverflow.ellipsis,
                                                          style: GoogleFonts.raleway(
                                                            fontSize: 15,
                                                          ),
                                                        )),
                                                    Flexible(
                                                        child: Text(
                                                          guide.email,
                                                          overflow: TextOverflow.ellipsis,
                                                          style: GoogleFonts.raleway(
                                                            fontSize: 15,
                                                          ),
                                                        )),
                                                  ],
                                                ),
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                  );
                                },
                              );
                            }
                          }
                          if(snapshot.hasError){
                            return Container(
                              child: Text("Page Not Found"),
                            );
                          }
                        }
                        return Center(child: CircularProgressIndicator());
                      }
                  ),
                );
              },
            )
          ],
        ),
      ),
    );
  }
}
