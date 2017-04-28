# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_maxbin(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_max_bin(self, params, context=None):
        """
        :param params: instance of type "MaxBinInputParams" (required params:
           assembly_ref: Genome assembly object reference binned_contig_name:
           BinnedContig object name and output file header workspace_name:
           the name of the workspace it gets saved to. reads_list: list of
           reads object (PairedEndLibrary/SingleEndLibrary) upon which MaxBin
           will be run optional params: thread: number of threads; default 1
           reassembly: specify this option if you want to reassemble the
           bins. note that at least one reads file needs to be designated.
           prob_threshold: minimum probability for EM algorithm; default 0.8
           markerset: choose between 107 marker genes by default or 40 marker
           genes min_contig_length: minimum contig length; default 1000
           plotmarker: specify this option if you want to plot the markers in
           each contig ref:
           http://downloads.jbei.org/data/microbial_communities/MaxBin/README.
           txt) -> structure: parameter "assembly_ref" of type "obj_ref" (An
           X/Y/Z style reference), parameter "binned_contig_name" of String,
           parameter "workspace_name" of String, parameter "reads_list" of
           list of type "obj_ref" (An X/Y/Z style reference), parameter
           "thread" of Long, parameter "reassembly" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "prob_threshold" of Double, parameter "markerset" of Long,
           parameter "min_contig_length" of Long, parameter "plotmarker" of
           type "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of type "MaxBinResult" (result_folder: folder path
           that holds all files generated by run_max_bin report_name: report
           name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "result_directory" of String, parameter "binned_contig_obj_ref" of
           type "obj_ref" (An X/Y/Z style reference), parameter "report_name"
           of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_maxbin.run_max_bin',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_maxbin.status',
                                        [], self._service_ver, context)
