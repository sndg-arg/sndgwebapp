import 'bootstrap/dist/css/bootstrap.css';
import "msa/css/msa.css";


//import Phylocanvas from 'phylocanvas';
import $ from 'jquery';
import Fasta from 'biojs-io-fasta';


import msa from "msa";
//import phylocanvas from "@phylocanvas/phylocanvas.gl"
import PhylocanvasGL, { TreeTypes } from "@phylocanvas/phylocanvas.gl";
//import metadata from 'phylocanvas-plugin-metadata';

//Phylocanvas.plugin(metadata);

import blasterjs from 'biojs-vis-blasterjs';

window.$ = $;
window.msa = msa;
window.blasterjs = blasterjs;
//window.Phylocanvas = Phylocanvas;
window.PhylocanvasGL = PhylocanvasGL;
window.TreeTypes = TreeTypes;
window.Fasta = Fasta;
import SeqView from "sequence-viewer";

window.SeqView = SeqView;

import FeatureViewer from 'feature-viewer';

window.FeatureViewer = FeatureViewer;

import {Stage as NGL} from 'ngl'
window.NGL = NGL;

/*

window.customElements.define("protvista-track", ProtvistaTrack);
export default (name, constructor) => {
  if (!window.customElements.get(name)) {
    window.customElements.define(name, constructor);
  }
};

* */




