from client import ModularB2bProcurementMarketplacePortalClient

def main():
    client = ModularB2bProcurementMarketplacePortalClient()
    res = client.configure_enterprise_procurement_portal('Saint-Gobain Building Materials', 120000)
    print('Portal Config: ' + res['portal_configuration_id'] + ' for ' + res['buyer_company'])
    print('Procurement Time Saved: -' + str(res['procurement_cycle_time_reduced_pct']) + '% | Approvals: ' + str(res['multi_tier_approval_hierarchy_levels']) + ' tiers')
    print('cXML Punchout SAP/Ariba: ' + str(res['punchout_cxml_sap_ariba_integrated']))

if __name__ == '__main__':
    main()
