# import cocotb
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_systolic_array(dut): 

    # Create a clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # rst the DUT (device under test)
    dut.rst.value = 1
    dut.load_weights.value = 0
    dut.weight_11.value = 0
    dut.weight_12.value = 0

    dut.weight_21.value = 0
    dut.weight_22.value = 0

    dut.input_11.value = 0
    dut.input_21.value = 0
    dut.start.value = 0
    await Timer(10, units="ns")

    dut.rst.value = 0
    await Timer(10, units="ns")

    dut.load_weights.value = 1
    dut.weight_11.value = 1
    dut.weight_12.value = 3
    dut.weight_21.value = 2
    dut.weight_22.value = 4
    await Timer(10, units="ns")

    dut.start.value = 1 
    dut.load_weights.value = 0

    await Timer(10, units="ns") 
    dut.input_11.value = 5
    dut.input_21.value = 0

    await Timer(10, units="ns")
    dut.input_11.value = 0
    dut.input_21.value = 6

    await Timer(10, units="ns")
    dut.input_11.value = 0
    dut.input_21.value = 0

    await Timer(10, units="ns")
    dut.input_11.value = 0
    dut.input_21.value = 0

    await Timer(10, units="ns")
    dut.input_11.value = 0
    dut.input_21.value = 0

    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")

    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")
    await Timer(10, units="ns")
