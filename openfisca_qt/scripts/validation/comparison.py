# -*- coding:utf-8 -*-
# Created on 17 févr. 2013
# This file is part of OpenFisca.
# OpenFisca is a socio-fiscal microsimulation software
# Copyright © #2013 Clément Schaff, Mahdi Ben Jelloul
# Licensed under the terms of the GVPLv3 or later license
# (see openfisca/__init__.py for details)

from __future__ import division

from openfisca_core.simulations import SurveySimulation
from openfisca_france.data.erf.datatable import ErfsDataTable


    #def test_demography():
    #    #  Demographic characteristics
    #    #    number of households/foyers compared to erf (and other sources recensement ? careful with champm variable)
    #
    #    merged_df["diff"] = merged_df["af"] - merged_df["m_afm"]
    #    print merged_df["diff"].describe()
    #    print "non nul :", (merged_df["diff"] != 0).sum()
    #    print " < -400 :", (merged_df["diff"] <= -400).sum()
    #    diff = merged_df.loc[merged_df["diff"] != 0, ["diff","wprm"]]
    #    print diff.describe(percentile_width=80)
    #    return
    #
    #
    #    wprm_of_men = wprm.sum()
    #    wprm_erf_men = df.wprm.sum()
    #    print wprm_erf_men, wprm_of_men
    #
    #    wprm_champm_of_men = (wprm*champm).sum()
    #    wprm_champm_erf_men = (df.wprm*df.champm).sum()
    #    print wprm_champm_erf_men, wprm_champm_of_men
    #
    #    af_of_men = (af.af).sum()
    #    af_erf_men = (df["m_afm"]).sum()
    #    print af_erf_men/1e9, af_of_men/1e9
    #
    #
    #    df = df.astype('float64')
    #
    #    af_of_men = (af.af*wprm).sum()
    #    af_erf_men = (df["m_afm"]*df.wprm*df.champm).sum()
    #    print af_erf_men/1e9, af_of_men/1e9
    #
    #
    #    #    types of household compared to erf
    #    #    age structure of population  scripts.sandbox.age_structure.py
    #
    #
    #
    #
    #    # Post-computation validation
    #    #
    #    #  Check for every prestation the equivalence/differneces of concept definition
    #    #  Decompose cotsoc (in the code TODO: MBJ LB ?)
    #    #  Decompose impot sur le revenu to check intermediate aggregates vs fiscal data and erf
    #    #  Check downward prestation one by one

def get_common_dataframe(variables, year = 2006):
    """
    Compare variables in erf an openfisca
    """
    simulation = SurveySimulation()
    simulation.set_config(year = year)
    simulation.set_param()
    simulation.set_survey()
    simulation.compute()

    erf = ErfsDataTable(year=2006)
    if "ident" not in variables:
        erf_variables = variables + ["ident"]
    else:
        erf_variables = variables

    if "wprm" not in erf_variables:
        erf_variables = erf_variables + ["wprm"]
    else:
        erf_variables = erf_variables

    erf_dataframe = erf.get_values(erf_variables, table="menage")
    erf_dataframe.rename(columns={'ident': 'idmen'}, inplace=True)
    for col in erf_dataframe.columns:
        if col is not "idmen":
            erf_dataframe.rename(columns={col: col + "_erf"}, inplace=True)

    of_dataframe, of_dataframe_default = simulation.aggregated_by_entity("men", variables, all_output_vars=False, force_sum=True)
    del of_dataframe_default

    merged_df = of_dataframe.merge(erf_dataframe, on="idmen")
    del of_dataframe, erf_dataframe
    return merged_df


def af():
    variables = [ "af_base", "af_majo", "af_forf", "af"]
    df = get_common_dataframe(variables)
    print df[["af", "af_base", "af_majo", "af_forf", "m_afm_erf"]].describe()
    df["diff"] = df.af -df.m_afm_erf
    print (df.af_base*df.wprm).sum()
    print (df.af*df.wprm).sum()
    print (df.m_afm_erf*df.wprm).sum()

    df_neg = df[ df["diff"]< 0]

    print df_neg["diff"].describe()
    sorted_df = df_neg.sort(columns=["diff"])
    print sorted_df[["idmen","af", "af_base", "af_majo", "af_forf", "m_afm_erf", "diff"]].head(50)



def cf():
    variables = [ "cf", "af_nbenf"]
    df = get_common_dataframe(variables)
    print df[["cf", "m_cfm_erf"]].describe()
    df["diff"] = df.cf -df.m_cfm_erf
    print (df.cf*df.wprm).sum()
    print (df.m_cfm_erf*df.wprm).sum()
    print df.describe()

    df_neg =  df[ (df.cf -df.m_cfm_erf) < 0]
    print df_neg.describe()


    grouped = df_neg.groupby( by="af_nbenf")
    print grouped.agg({'wprm' : ['sum', 'count'], 'cf' : "mean", "m_cfm_erf" : "mean"} )

#    sorted_df = df_neg.sort(columns=["diff"])

    for name, group in grouped:
        print name
        sorted_group = group.sort(columns=["diff"])
        print sorted_group[["idmen", "cf", "m_cfm_erf", "diff"]].head(50)

    return df_neg["idmen"].values

def get_menage(idmen):
    erf = ErfsDataTable(year=2006)
    erf_variables = ["ident", "age", "noi", "persfip", "persfipd","quelfic", "declar1", "declar2"]
    dataframe = erf.get_values(erf_variables, table="indivi")
    dataframe.rename(columns={'ident': 'idmen'}, inplace=True)
    selection = dataframe.idmen == idmen
    return dataframe[selection]

if __name__ == '__main__':

#    test_demography()
#    cf()

#    idmens = [6000774, 6005865, 6006829, 6007038, 6007645, 6008137, 6008426, 6009565,
#              6009834, 6014137, 6014845, 6019038, 6020266, 6022087, 6023336, 6027342,
#              6028276, 6028448, 6029882, 6031162, 6034631, 6002569]

    idmens = cf()
    print idmens
    for idmen in idmens:
        df = get_menage(idmen)
        no_declar = df["declar1"].isnull().all() & df["declar2"].isnull().all()
        double_declar = df["persfipd"].notnull().any()
#        if no_declar: print "no_declar"
#        elif double_declar: print "double_declar"
#        else :
#            print "WRONG"
#            print df
#            print "-----"
        if not(no_declar or double_declar):
            print "WRONG"
            print df
            print "-----"

