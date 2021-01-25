package com.example.accelerometer_gyroscope


import android.content.Context
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity


class MainActivity : AppCompatActivity(), SensorEventListener {
    private lateinit var sensorManager: SensorManager
    private var mAcc: Sensor? = null
    private var mGyr: Sensor? = null
    private lateinit var tv11: TextView
    private lateinit var tv12: TextView
    private lateinit var tv13: TextView
    private lateinit var tv21: TextView
    private lateinit var tv22: TextView
    private lateinit var tv23: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
        mAcc = sensorManager.getDefaultSensor(Sensor.TYPE_LINEAR_ACCELERATION)
        mGyr = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE)
    }

    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {

    }

    override fun onSensorChanged(event: SensorEvent) {
        when (event.sensor.type){
            Sensor.TYPE_LINEAR_ACCELERATION -> {
                val x = event.values[0]
                val y = event.values[1]
                val z = event.values[2]
                tv11= findViewById(R.id.x_coord1)
                tv11.setText(if (x<0) "%.5f".format(x) else " %.5f".format(x))
                tv12= findViewById(R.id.y_coord1)
                tv12.setText(if (y<0) "%.5f".format(y) else " %.5f".format(y))
                tv13= findViewById(R.id.z_coord1)
                tv13.setText(if (z<0) "%.5f".format(z) else " %.5f".format(z))

            }
            Sensor.TYPE_GYROSCOPE -> {
                val x = event.values[0]
                val y = event.values[1]
                val z = event.values[2]

                tv21= findViewById(R.id.x_coord2)
                tv21.setText(if (x<0) "%.5f".format(x) else " %.5f".format(x))
                tv22 = findViewById(R.id.y_coord2)
                tv22.setText(if (y<0) "%.5f".format(y) else " %.5f".format(y))
                tv23= findViewById(R.id.z_coord2)
                tv23.setText(if (z<0) "%.5f".format(z) else " %.5f".format(z))

            }
            else -> print("sth else")
        }
    }
    override fun onStart(){
        super.onStart()
        if (mAcc != null){
            sensorManager.registerListener(this, mAcc, SensorManager.SENSOR_DELAY_UI)
        }
        if (mGyr != null){
            sensorManager.registerListener(this, mGyr, SensorManager.SENSOR_DELAY_UI)
        }
    }
    override fun onStop() {
        super.onStop()
        sensorManager.unregisterListener(this)
    }
}