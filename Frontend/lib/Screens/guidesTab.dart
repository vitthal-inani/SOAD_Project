import 'package:flutter/material.dart';
import 'package:travel/Models/City.dart';
import 'package:travel/Models/Guides.dart';
import 'package:travel/Tools/Global%20tools.dart';
import 'package:syncfusion_flutter_datepicker/datepicker.dart';
import 'package:travel/Tools/GuideFilter.dart';

class GuidesTab extends StatelessWidget {
  Guide guide = Guide.fromJSON({
    "guide_name": "Chandler Bing",
    "guide_id": 2,
    "rating": 3.0,
    "monument_names": ["Monument A","Monument B"],
    "imageURL": "https://image.shutterstock.com/image-vector/young-man-face-cartoon-260nw-1224888760.jpg"
  });
  // GuidesTab({this.guide});

  @override
  Widget build(BuildContext context) {
    final _screenSize = MediaQuery.of(context).size;
    return Container(
      padding: EdgeInsets.all(20),
      child: Column(
        children: [
          //  guide filter
          GuideFilter(
            width: _screenSize.width*0.2,
          ),
          Padding(
            padding: EdgeInsets.all(_screenSize.height * 0.01),
          ),
          //  cards
          Container(
            height: _screenSize.height * 0.6,
            child: ListView.separated(
              shrinkWrap: true,
              itemCount: 8,
              separatorBuilder: (context, idx) {
                return Padding(
                  padding: EdgeInsets.all(10),
                );
              },
              itemBuilder: (context, idx) {
                return Card(
                  elevation: 10,
                  child: Container(
                    height: _screenSize.height * 0.3,
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
                                  guide.guideName,
                                  overflow: TextOverflow.ellipsis,
                                  style: TextStyle(fontSize: 30),
                                )),
                                // Text(
                                //   "State: " + monument.state,
                                //   overflow: TextOverflow.ellipsis,
                                //   style: TextStyle(fontSize: 20),
                                // ),
                                // Flexible(
                                //     child: Text(
                                //   monument.info,
                                //   style: TextStyle(fontSize: 15),
                                // )),
                              ],
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          )
        ],
      ),
    );
  }
}
