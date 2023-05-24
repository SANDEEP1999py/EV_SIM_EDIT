import unittest

import numpy as np

import EV_sim


class TestEVObject(unittest.TestCase):
    def test_EV_contructors(self):
        alias_name = "Volt_2017"
        volt = EV_sim.EV(alias_name=alias_name)
        # Check for vehicle basic information
        self.assertEqual(alias_name, volt.alias_name)
        self.assertEqual("Volt", volt.model_name)
        self.assertEqual("2017", volt.year)
        self.assertEqual("Chevy", volt.manufacturer)
        # Check for vehicle drivetrain information
        self.assertEqual(0.35, volt.drive_train.wheel.r)
        self.assertEqual(8.0, volt.drive_train.wheel.I)
        self.assertEqual(4, volt.drive_train.num_wheel)
        self.assertEqual(0.94, volt.drive_train.inverter_eff)
        self.assertEqual(0.9, volt.drive_train.frac_regen_torque)
        self.assertEqual(0.97, volt.drive_train.eff)
        # Check for motor information
        self.assertEqual(4000.0, volt.motor.RPM_r)
        self.assertEqual(12000, volt.motor.RPM_max)
        self.assertEqual(275.0, volt.motor.L_max)
        self.assertEqual(0.2, volt.motor.I)
        self.assertEqual(0.95, volt.motor.eff)
        # Check for battery pack information
        self.assertTrue(np.isnan(volt.pack.cell_manufacturer))
        self.assertEqual(15.0, volt.pack.cell_cap)
        self.assertEqual(450.0, volt.pack.cell_mass)
        self.assertEqual(4.2, volt.pack.cell_V_max)
        self.assertEqual(3.8, volt.pack.cell_V_nom)
        self.assertEqual(3, volt.pack.cell_V_min)
        self.assertEqual(3, volt.pack.Np)
        self.assertEqual(8, volt.pack.Ns)
        self.assertEqual(0.08, volt.pack.module_overhead_mass)
        self.assertEqual(12, volt.pack.num_modules)
        self.assertEqual(0.1, volt.pack.pack_overhead_mass)
        self.assertEqual(75, volt.pack.SOC_full)
        self.assertEqual(25, volt.pack.SOC_empty)
        self.assertEqual(0.96, volt.pack.eff)
        # Check for other vehicle information
        self.assertEqual(0.0111, volt.C_r)
        self.assertEqual(0.22, volt.C_d)
        self.assertEqual(1425.0, volt.m)
        self.assertEqual(75.0, volt.payload_capacity)
        self.assertEqual(200.0, volt.overhead_power)

    def test_property_attributes(self):
        alias_name = "Volt_2017"
        volt = EV_sim.EV(alias_name=alias_name)
        self.assertEqual(1581.5217391304348, volt.curb_mass)
        self.assertEqual(1656.5217391304348, volt.max_mass)
        self.assertEqual(555.1020408163266, volt.rot_mass)
        self.assertEqual(2211.6237799467613, volt.equiv_mass)
        self.assertEqual(131.94689145077132, volt.max_speed)