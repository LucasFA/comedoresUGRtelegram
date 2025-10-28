{
  description = "A template that shows all standard flake outputs";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

 outputs = { self, nixpkgs, utils }:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      # eachSystem = f: nixpkgs.lib.genAttrs (import systems) (system: f nixpkgs.legacyPackages.${system});
      # treefmtEval = eachSystem (pkgs: treefmt-nix.lib.evalModule pkgs ./modules/treefmt);
      in
      {
        devShell = with pkgs; mkShellNoCC {
          buildInputs = [
            uv
          ];
        };
      }
    );
}
