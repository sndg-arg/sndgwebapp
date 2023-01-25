import 'bootstrap/dist/css/bootstrap.css';
import "msa/css/msa.css";


import Phylocanvas from 'phylocanvas';
import $ from 'jquery';
import Fasta from 'biojs-io-fasta';


import msa from "msa";
import metadata from 'phylocanvas-plugin-metadata';

Phylocanvas.plugin(metadata);

window.$ = $;
window.msa = msa;
window.Phylocanvas = Phylocanvas;
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




