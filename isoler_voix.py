#!/usr/bin/env python3
"""
Séparateur de voix avec Spleeter
Isole les voix et l'accompagnement musical d'un fichier audio
"""

from spleeter.separator import Separator
import os
import sys


def isoler_voix(chemin_audio, dossier_sortie="audio_separe", modele="2stems"):
    """
    Sépare la voix de l'accompagnement musical

    Args:
        chemin_audio (str): Chemin vers le fichier audio
        dossier_sortie (str): Dossier de sortie
        modele (str): Modèle Spleeter ('2stems', '4stems', '5stems')
    """

    # Vérifier que le fichier existe
    if not os.path.exists(chemin_audio):
        print(f"❌ Fichier introuvable : {chemin_audio}")
        return False

    # Vérifier l'extension du fichier
    extensions_valides = ['.mp3', '.wav', '.flac', '.m4a']
    if not any(chemin_audio.lower().endswith(ext) for ext in extensions_valides):
        print(f"❌ Format non supporté. Utilisez : {', '.join(extensions_valides)}")
        return False

    try:
        # Initialiser le séparateur
        print(f"🛠️ Initialisation du modèle {modele}...")
        separator = Separator(f'spleeter:{modele}-16kHz')

        # Créer le dossier de sortie s'il n'existe pas
        os.makedirs(dossier_sortie, exist_ok=True)

        # Traitement
        print(f"🎵 Traitement de : {os.path.basename(chemin_audio)}")
        print("⏳ Cela peut prendre quelques minutes...")

        separator.separate_to_file(chemin_audio, dossier_sortie)

        print("✅ Séparation terminée !")
        print(f"📁 Résultats disponibles dans : {dossier_sortie}")

        # Lister les fichiers créés
        nom_fichier = os.path.splitext(os.path.basename(chemin_audio))[0]
        chemin_resultat = os.path.join(dossier_sortie, nom_fichier)

        if os.path.exists(chemin_resultat):
            fichiers = os.listdir(chemin_resultat)
            print("\n📄 Fichiers créés :")
            for fichier in fichiers:
                print(f"   • {fichier}")

        return True

    except Exception as e:
        print(f"❌ Erreur lors du traitement : {e}")
        return False


def main():
    """Interface en ligne de commande"""
    print("🎤 Séparateur de voix avec Spleeter")
    print("=" * 40)

    if len(sys.argv) > 1:
        # Utiliser l'argument de ligne de commande
        fichier_audio = sys.argv[1]
    else:
        # Demander à l'utilisateur
        fichier_audio = input("\n📁 Chemin vers votre fichier audio : ").strip().strip('"')

    if not fichier_audio:
        print("❌ Aucun fichier spécifié")
        return

    # Choisir le modèle
    print("\n🎛️ Modèles disponibles :")
    print("  1. 2stems - Voix + Accompagnement (recommandé)")
    print("  2. 4stems - Voix + Batterie + Basse + Autres")
    print("  3. 5stems - Voix + Batterie + Basse + Piano + Autres")

    choix = input("\nChoisissez un modèle (1-3) [1] : ").strip()

    if choix == "2":
        modele = "4stems"
    elif choix == "3":
        modele = "5stems"
    else:
        modele = "2stems"

    # Dossier de sortie
    dossier_sortie = input(f"\n📂 Dossier de sortie [audio_separeted] : ").strip()
    if not dossier_sortie:
        dossier_sortie = "audio_separeted"

    # Traitement
    print(f"\n🚀 Démarrage avec le modèle {modele}...")
    succes = isoler_voix(fichier_audio, dossier_sortie, modele)

    if succes:
        print(f"\n🎉 Terminé ! Vos fichiers sont dans '{dossier_sortie}'")
    else:
        print("\n💥 Échec du traitement")


if __name__ == "__main__":
    main()