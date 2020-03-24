class TomlDictForCSVformatter:

    """ A class for storing dictionary of settings for formatting CSV after being extracted using
    :class:`gis2csv`. Takes no argument. 
    """

    def __init__(self):

        """ Constrcutor method for :class:TomlDictForCSVformatter"""

        self.toml_dict = {
            "GIScsvsfolderpath" : "C:\\Users\\KDUWADI\\Desktop\\NREL_Projects\\CIFF-TANGEDCO\\TANGEDCO\\SoftwareTools\\GIS_CSVs_to_Standard_CSVs",
            "feeder_name" : "GWC",
            "MVA_to_KVA_conversion_for_PT"  : "yes",
            "force_lt_be_three_phase" : "yes",
            "PTrow" :  0,
            "three_phase" : "RYB",
            "single_phase" : ["R","Y","B"],
            "height_of_top_conductor_ht" : 9,
            "height_of_top_conductor_lt" : 8,
            "ht_spacing" : 1,
            "lt_spacing" : 0.47,
            "geomtry_units" : 'm',
            "Service_wire_single_phase" : {
                "conductor_spacing" : 0.47,
                "num_of_cond" : 2,
                "num_of_phases" : 1, 
                "height_of_top_conductor": 8,
                "phase_conductor":"AAAC_4.0",
                "neutral_conductor" : "AAAC_4.0",
                "units": "m",
                "spacing": "vertical",
            },
            "Service_wire_three_phase": {
                "conductor_spacing" : 0.47,
                "num_of_cond" : 4,
                "num_of_phases" : 3, 
                "height_of_top_conductor": 8,
                "phase_conductor": "AAAC_4.0",
                "neutral_conductor" : "AAAC_4.0",
                "units": "m",
                "spacing": "vertical",
            },
            "ht_three_phase" : {
                "conductor_spacing" : 1,
                "num_of_cond" : 3,
                "num_of_phases" : 3,
                "height_of_top_conductor": 9,
                "phase_conductor": "RABBIT_7/3.35",
                "neutral_conductor" : "RABBIT_7/3.35",
                "units": "m",
                "spacing":"vertical",
            },
            "Consumer_kv": {
                'ht_consumer_ll' : 11.0,
                'ht_consumer_phase' : 6.6,
                'lt_consumer_ll' : 0.44,
                'lt_consumer_phase' : 0.23,
            },
            "load_type": {
                "lt_consumer" : "wye",
                "ht_consumer" : "delta",
            },
            'ht_line': {
                "node_file_name" : "Asset_HT_Line_node.csv",
                "attribute_file_name" : "Asset_HT_Line_attribute.csv",
            },
            'ht_cable': {
                "node_file_name" : "Asset_HT_Line_Cable_node.csv",
                "attribute_file_name" : "Asset_HT_Line_Cable_attribute.csv",
            },
            'lt_line':{
                "node_file_name" : "Asset_LT_Line_node.csv",
                "attribute_file_name" : "Asset_LT_Line_attribute.csv",
            },
            'lt_cable':{
                "node_file_name" : "Asset_LT_Line_Cable_node.csv",
                "attribute_file_name" : "Asset_LT_Line_Cable_attribute.csv",
            },
            "line_column_mapper": {
                "length" : ["SHAPE_Leng"],
                "phase" :  ["force","RYB"],  
                "four_conductor_system" : ["3Ph Five wire system","3Ph Four wire system"],
                "three_conductor_system" : ["3Ph Three wire system"],
                "two_conductor_system" : ["1Ph Three wire system","1Ph Two wire system","2Ph Three wire system"],
                "phase_system" : ["HTL_PWS","HTLC_PWS","LTL_PWS","LTLC_PWS"],
                "csize" : ["HTL_CSIZE_","HTLC_CBL_S","LTL_CSIZE","LTLC_CBL_S"],
                "cname" : ["HTL_CNAME","HTLC_CBL_T","LTL_CNAME","LTLC_CBL_T"],
                "nsize" : ["LTL_N_CSIZ"],
                "nname" : ["LTL_N_CNAM"],
                "units" : ["force","m"],  
                "spacing" : ["force","vertical"],
            },
            "distribution_transformer":{"file_name" : "Asset_Distribution_Transformer.csv"},
            "power_transformer":{"file_name" : "Asset_Power_Transformer.csv"},
            "transformer_column_mapper": {
                "ID"  : ["DT_ID","PTR_ID"],
                "KVA_cap" : ["DT_CC_KVA","PTR_CAP_MV"],
                "HV_KV" : ["DT_HVSV_KV","PTR_PRY_VO"],
                "LV_KV" : ["DT_LVSV_KV","PTR_SEC_VO"],
                "maxtap" : ["force","1.1"],
                "mintap" : ["force","0.9"],
                "tap" : ["force","1.0"],
                "numtaps" : ["force","10"],
                "prim_con" : ["force","delta"],
                "sec_con" : ["force","wye"],
                "vector_group" : ["force","Dyn11"],
                "%resistance" : ["force","0.75"],
                "%reactance" : ["force","7.5"],
                "%noloadloss" : ["force","0"],
                "phase" : ["force","RYB"],
                "x" : ["x"],
                "y" : ["y"],
            },
            "lt_consumer": {"file_name" : "Consumer_LT.csv"},
            "ht_consumer":{"file_name" : "Consumer_HT.csv"},
            "consumer_column_mapper": {
                "pf" : ["LTC_PF","HTC_PF"],
                "tariff_type" : ["LTC_TCODE","HTC_TCODE"],
                "phase": ["LTC_PHASE","HTC_PHASE"],
                "Sanctioned_load" : ["LTC_SLOAD_","HTC_SDEMAN"],
                "x" : ["x"],
                "y" : ["y"],
                "PeakMWload" :  1.2,
                "estimate_consumer_peakkw" : "yes",
            },
            "consumer_class_by_tariff":{
                "residential" : ["LT Tariff IA","LT Tariff I B","LT Tariff VI"],
                "commercial" : ["LT Tariff II-A","LT Tariff II-B(1)","LT Tariff II-C", "LT Tariff V","LT Tariff II-B(2"],
                "industrial" : ["LT Tariff III-A (1)", "LT Tariff III-B","TARIFF III"],
                "agricultural" : ["LT Tariff IV"],
            },
            "peak_contribution": {
                "residential" : 0.867,
                "commercial" : 0.105,
                "industrial" : 0.017,
                "agricultural" : 0.011,
            },
            "tec_per_kw_by_consumer_type":{
                "residential" : 5937.831,
                "commercial" : 6168.84,
                "industrial" : 6206.385,
                "agricultural" : 6102.5,
            },
        }

    def ReturnDict(self):

        """ Returns a dictionary which can be converted into Toml file necessary for CSV formatting
        :return: A dictionary of settings for CSV formatting
        :rtype: dict
        
        """

        return self.toml_dict