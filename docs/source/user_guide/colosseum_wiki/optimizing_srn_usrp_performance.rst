Optimizing SRN USRP Performance
============================

Use LO Offset Tuning
~~~~~~~~~~~~~~~~~~~~

NI recommends using an LO Offset of -42 MHz for TX and +42 MHz for RX. See figures below.

TX Settings
^^^^^^^^^^^

.. figure:: /_static/images/user_guide/wiki/optimizing-srn-usrp-performance/tx_settings.png
   :alt: TX Settings
   :align: center

**For teams using the device3 API (RFNoC):**

Offset LO tuning has to be done in two steps because the radio and the digital upconverter (DUC) blocks have separate frequency configuration APIs.

.. code-block:: cpp

   uhd::rfnoc::radio_ctrl::sptr radio_blk;
   uhd::rfnoc::duc_block_ctrl::sptr duc_blk;
   …
   double center_freq = 1.0e9
   double lo_offset = -42.e6;
   radio_blk->set_tx_frequency(center_freq + lo_offset);
   duc_blk->set_arg("freq", -lo_offset);   //NOTE: lo_offset is negated

RX Settings
^^^^^^^^^^^

.. figure:: /_static/images/user_guide/wiki/optimizing-srn-usrp-performance/rx_settings.png
   :alt: RX Settings
   :align: center

**For teams using the device3 API (RFNoC):** Offset LO tuning has to be done in two steps because the radio and the digital downconverter (DDC) blocks have separate frequency configuration APIs.

.. code-block:: cpp

   uhd::rfnoc::radio_ctrl::sptr radio_blk;
   uhd::rfnoc::ddc_block_ctrl::sptr ddc_blk;
   …
   double center_freq = 1.0e9
   double lo_offset = +42.e6;
   radio_blk->set_rx_frequency(center_freq + lo_offset);
   ddc_blk->set_arg("freq", lo_offset);

Use optimal ADC/DAC settings to maximize dynamic range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use optimal ADC/DAC settings to maximize dynamic range for UBX-LP UBX-LP link. NI's recommendation is to increase the ADC gain and decrease DAC full-scale current. 

**For users using vanilla/unmodified UHD:**

- See the attached patch for older versions of UHD, including the default LTS version in Colosseum, UHD 3.9.x:
   - x300-Optimal-ADC-DAC-settings-for-Colosseum-SRNs_UHD-3.9.x.patch
- For teams using a more recent version of UHD 3.10.x:
   - x300-Optimal-ADC-DAC-settings-Colosseum-SRNs_UHD-3.10.x.patch
- How-to install patch: (1) download your patch from above (attachments found at bottom of page), (2) run "patch < patchfile"

**For teams using a custom modified version of UHD** 3.10.x or higher, or the rfnoc-devel branch, the following patches (files attached below) can be applied individually so that they are agnostic to the git hash or version:

- x300-Optimal-ADC-DAC-settings-Colosseum-SRNs_UHD-NOVER_x300_dac_ctrl.cpp.patch
- x300-Optimal-ADC-DAC-settings-Colosseum-SRNs_UHD-NOVER_x300_radio_ctrl_impl.cpp.patch

**Commands:**

.. code-block:: bash

   patch /host/lib/usrp/x300/x300_dac_ctrl.cpp x300-Optimal-ADC-DAC-settings-Colosseum-SRNs_UHD-NOVER_x300_dac_ctrl.cpp.patch
   patch /host/lib/usrp/x300/x300_radio_ctrl_impl.cpp x300-Optimal-ADC-DAC-settings-Colosseum-SRNs_UHD-NOVER_x300_radio_ctrl_impl.cpp.patch

Use optimal RF gain to maximize dynamic range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NI has determined that the optimal RX and TX gain settings for the UBX-LP UBX-LP link vary across frequency. See below for the recommended settings at some common frequencies. 

- 1.0 GHz => TX Gain: **20 dB**, RX Gain: **7 dB**
- 2.4 GHz => TX Gain: **23 dB**, RX Gain: **8 dB**
- 5.8 GHz => TX Gain: **28 dB**, RX Gain: **15 dB**
