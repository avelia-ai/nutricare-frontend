package fr.mirella.app;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.PermissionState;
import com.getcapacitor.annotation.CapacitorPlugin;
import com.getcapacitor.annotation.Permission;
import com.getcapacitor.annotation.PermissionCallback;

@CapacitorPlugin(
    name = "StepCounter",
    permissions = {
        @Permission(strings = { "android.permission.ACTIVITY_RECOGNITION" }, alias = "activityRecognition")
    }
)
public class StepCounterPlugin extends Plugin implements SensorEventListener {
    private SensorManager sensorManager;
    private Sensor stepSensor;
    private PluginCall pendingCall;

    @Override
    public void load() {
        sensorManager = (SensorManager) getContext().getSystemService(Context.SENSOR_SERVICE);
        if (sensorManager != null) {
            stepSensor = sensorManager.getDefaultSensor(Sensor.TYPE_STEP_COUNTER);
        }
    }

    @PluginMethod
    public void getStepsSinceBoot(PluginCall call) {
        if (getPermissionState("activityRecognition") != PermissionState.GRANTED) {
            requestPermissionForAlias("activityRecognition", call, "stepsPermCallback");
            return;
        }
        readSteps(call);
    }

    @PermissionCallback
    private void stepsPermCallback(PluginCall call) {
        if (getPermissionState("activityRecognition") == PermissionState.GRANTED) {
            readSteps(call);
        } else {
            JSObject ret = new JSObject();
            ret.put("available", false);
            ret.put("error", "permission_denied");
            call.resolve(ret);
        }
    }

    private void readSteps(PluginCall call) {
        if (stepSensor == null) {
            JSObject ret = new JSObject();
            ret.put("available", false);
            ret.put("error", "no_sensor");
            call.resolve(ret);
            return;
        }
        this.pendingCall = call;
        sensorManager.registerListener(this, stepSensor, SensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        if (event == null || event.sensor.getType() != Sensor.TYPE_STEP_COUNTER) return;
        float steps = event.values[0];
        sensorManager.unregisterListener(this);
        if (pendingCall != null) {
            JSObject ret = new JSObject();
            ret.put("available", true);
            ret.put("stepsSinceBoot", (int) steps);
            pendingCall.resolve(ret);
            pendingCall = null;
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {}
}
