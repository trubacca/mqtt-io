"""
AS7341 Spectral Analyser
Ref: https://circuitpython.readthedocs.io/projects/as7341/en/latest/examples.html

"""

from typing import cast

from ...types import ConfigType, SensorValueType
from . import GenericSensor
from ...exceptions import RuntimeConfigError

REQUIREMENTS = ("adafruit-circuitpython-as7341",)


class Sensor(GenericSensor):
    """
    Implementation of Sensor class for AS7341.
    """

    SENSOR_SCHEMA = {
        "type": dict(
            type="string",
            required=False,
            empty=False,
            default="channel_clear",
            allowed=[
                "channel_clear",
                "channel_415nm",
                "channel_445nm",
                "channel_480nm",
                "channel_515nm",
                "channel_555nm",
                "channel_590nm",
                "channel_630nm",
                "channel_680nm",
                "channel_nir"
            ]
        )
    }

    def setup_module(self) -> None:
        # pylint: disable=import-outside-toplevel,import-error
        import adafruit_as7341  # type: ignore
        import board  # type: ignore
        import busio  # type: ignore

        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_as7341.AS7341(i2c)

    @property # F1 - 415nm/Violet 
    def _channel_415nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_415nm)

    @property # F2 - 445nm//Indigo
    def _channel_445nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_445nm)

    @property # F3 - 480nm//Blue
    def _channel_480nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_480nm)

    @property # F4 - 515nm//Cyan 
    def _channel_515nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_515nm)

    @property # F5 - 555nm/Green 
    def _channel_555nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_555nm)

    @property # F6 - 590nm/Yellow
    def _channel_590nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_590nm)

    @property # F7 - 630nm/Orange
    def _channel_630nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_630nm)

    @property # F8 - 680nm/Red 
    def _channel_680nm(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_680nm)

    @property
    def _channel_clear(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_clear)

    @property
    def _channel_nir(self) -> SensorValueType:
        return cast(SensorValueType, self.sensor.channel_nir)

    def get_value(self, sens_conf: ConfigType) -> SensorValueType:
        """
        Get the temperature value from the sensor
        """
        if sens_conf["type"] == "channel_415nm":
            return self._channel_415nm
        if sens_conf["type"] == "channel_445nm":
            return self._channel_445nm
        if sens_conf["type"] == "channel_480nm":
            return self._channel_480nm
        if sens_conf["type"] == "channel_515nm":
            return self._channel_515nm
        if sens_conf["type"] == "channel_555nm":
            return self._channel_555nm
        if sens_conf["type"] == "channel_590nm":
            return self._channel_590nm
        if sens_conf["type"] == "channel_630nm":
            return self._channel_630nm
        if sens_conf["type"] == "channel_680nm":
            return self._channel_680nm
        if sens_conf["type"] == "channel_clear":
            return self._channel_clear
        if sens_conf["type"] == "channel_nir":
            return self._channel_nir
        raise RuntimeConfigError(
            "AS7341 sensor '%s' was not configured to return a valid channel"
            % sens_conf["name"]
        )
