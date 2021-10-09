import 'package:flutter/material.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Crap verification',
      theme: ThemeData(
        primarySwatch: Colors.yellow,
      ),
      home: MyHomePage(title: 'Select a supplier and a consignment.'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String _supplier = '';
  String _consignment = '';

  List<String> _dataSuppliers = ["1", "2", "3"];

  void _getImages(){
    return null;
  }

Widget supplierSelection() {
        return ExpansionPanel(
          headerBuilder: (BuildContext context) {
            return ListTile(
              title: Text("Supplier"),
                        body: ListTile(
              title: Text("2"),
              trailing: const Icon(Icons.add),
              onTap: () {
                setState(() {
                  _dataSuppliers.removeWhere((String currentItem) => _supplier == currentItem);
                });
              }),

            );
          },
        );
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Select a supplier and a consignment:',
            ),
            supplierSelection(),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _getImages,
        tooltip: 'Increment',
        child: Icon(Icons.add),
    ),
    );
  }
}
