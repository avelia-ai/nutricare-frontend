package fr.mirella.app

import android.content.Context
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import com.getcapacitor.JSObject
import com.getcapacitor.Plugin
import com.getcapacitor.PluginCall
import com.getcapacitor.PluginMethod
import com.getcapacitor.annotation.CapacitorPlugin
import com.getcapacitor.annotation.Permission
import com.getcapacitor.annotation.PermissionCallback

@CapacitorPlugin(
    name = "StepCounter",
    permissions = [
        Permission(strings = ["android.permission.ACTIVITY_RECOGNITION"], alias = "activityRecognition")
    ]
)
class StepCounterPlugin : Plugin(), SensorEventListener {
    private var sensorManager: SensorManager? = null
    private var stepSensor: Sensor? = null
    private var lastValue: Float = -1f

    override fun load() {
        sensorManager = context.getSystemService(Context.SENSOR_SERVICE) as SensorManager
        stepSensor = sensorManager?.getDefaultSensor(Sensor.TYPE_STEP_COUNTER)
    }

    @PluginMethod
    fun getStepsSinceBoot(call: PluginCall) {
        if (getPermissionState("activityRecognition") != com.getcapacitor.PermissionState.GRANTED) {
            requestPermissionForAlias("activityRecognition", call, "stepsPermCallback")
            return
        }
        readSteps(call)
    }

    @PermissionCallback
    private fun stepsPermCallback(call: PluginCall) {
        if (getPermissionState("activityRecognition") == com.getcapacitor.PermissionState.GRANTED) {
            readSteps(call)
        } else {
            val ret = JSObject()
            ret.put("available", false)
            ret.put("error", "permission_denied")
            call.resolve(ret)
        }
    }

    private fun readSteps(call: PluginCall) {
        if (stepSensor == null) {
            val ret = JSObject()
            ret.put("available", false)
            ret.put("error", "no_sensor")
            call.resolve(ret)
            return
        }
        this.pendingCall = call
        sensorManager?.registerListener(this, stepSensor, SensorManager.SENSOR_DELAY_NORMAL)
    }

    private var pendingCall: PluginCall? = null

    override fun onSensorChanged(event: SensorEvent?) {
        if (event == null || event.sensor.type != Sensor.TYPE_STEP_COUNTER) return
        val steps = event.values[0]
        sensorManager?.unregisterListener(this)
        val ret = JSObject()
        ret.put("available", true)
        ret.put("stepsSinceBoot", steps.toInt())
        pendingCall?.resolve(ret)
        pendingCall = null
    }

    override fun onAccuracyChanged(sensor: Sensor?, accuracy: Int) {}
}
