# function header: function takes as its single argument the Nix package archive
# We "pin" the package archive to a specific version
{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/20.09.tar.gz") {} }:
# just to save ourselves some typing
with pkgs;
with pkgs.python38Packages;
let
  # celluloid is not in the Nix package archive, so we make our own build prescription
  celluloid = buildPythonPackage rec {
    pname = "celluloid";
    version = "0.2.0";
    # fetches a Python package from the Python Package Index
    src = fetchPypi {
      inherit pname version;
      # we download something from the internet and to make sure it's indeed what we
      # expect it to be, we check its hash
      sha256 = "568b1512c4a97483759e9436c3f3e5dc5566da350179aa1872992ec8d82706e1";
    };
    # celluloids only Python dependency is matplotlib
    propagatedBuildInputs = [ matplotlib ];
  };
in
  # the result of this function: a reproducible shell with all our dependencies
  pkgs.mkShell {
    buildInputs = [ pandas ipython celluloid numpy matplotlib python-dateutil ffmpeg];
  }
