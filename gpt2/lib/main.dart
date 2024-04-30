import 'package:flutter/material.dart';
import 'dart:ui' as ui;

void main() => runApp(MaterialApp(home: ChartPage()));

class ChartPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Simple Chart Example')),
      body: Center(
        child: CustomPaint(
          size: Size(400, 300),
          painter: LineChartPainter(),
        ),
      ),
    );
  }
}

class LineChartPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    var paint = Paint()
      ..color = Colors.blue
      ..strokeWidth = 2
      ..style = PaintingStyle.stroke;

    var path = Path();

    // Sample data points
    List<Offset> points = [
      Offset(50, 250),
      Offset(100, 200),
      Offset(150, 150),
      Offset(200, 100),
      Offset(250, 50),
      Offset(300, 25),
      Offset(350, 5),
    ];

    // Draw the line connecting the points
    path.moveTo(points.first.dx, points.first.dy);
    for (var point in points) {
      path.lineTo(point.dx, point.dy);
    }

    // Draw the path
    canvas.drawPath(path, paint);

    // Draw points as circles
    for (var point in points) {
      canvas.drawCircle(point, 5, paint..color = Colors.red);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

// 5

// import 'dart:ui';
// import 'package:flutter/material.dart';

// void main() {
//   runApp(MetricsApp());
// }

// class MetricsApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'Metrics Dashboard',
//       theme: ThemeData(
//         primarySwatch: Colors.blue,
//         visualDensity: VisualDensity.adaptivePlatformDensity,
//       ),
//       home: DashboardScreen(),
//     );
//   }
// }

// class DashboardScreen extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Metrics Dashboard'),
//       ),
//       body: MetricsChart(),
//     );
//   }
// }

// class MetricsChart extends StatelessWidget {
//   final List<double> dataPoints = [10, 20, 30, 20, 50, 80, 60, 30, 70, 40, 90];

//   @override
//   Widget build(BuildContext context) {
//     return CustomPaint(
//       painter: ChartPainter(dataPoints),
//       child: Container(
//         height: 200,
//       ),
//     );
//   }
// }

// class ChartPainter extends CustomPainter {
//   List<double> dataPoints;
//   ChartPainter(this.dataPoints);

//   @override
//   void paint(Canvas canvas, Size size) {
//     double maxData =
//         dataPoints.reduce((curr, next) => curr > next ? curr : next);
//     double minData =
//         dataPoints.reduce((curr, next) => curr < next ? curr : next);

//     final paint = Paint()
//       ..color = Colors.blue
//       ..strokeCap = StrokeCap.round
//       ..strokeWidth = 5.0;

//     final pointInterval = size.width / (dataPoints.length - 1);
//     final scaleFactor = size.height / (maxData - minData);

//     for (int i = 0; i < dataPoints.length - 1; i++) {
//       final startX = i * pointInterval;
//       final startY = size.height - (dataPoints[i] - minData) * scaleFactor;
//       final endX = (i + 1) * pointInterval;
//       final endY = size.height - (dataPoints[i + 1] - minData) * scaleFactor;
//       canvas.drawLine(
//         Offset(startX, startY),
//         Offset(endX, endY),
//         paint,
//       );
//     }
//   }

//   @override
//   bool shouldRepaint(covariant CustomPainter oldDelegate) {
//     return false;
//   }
// }
