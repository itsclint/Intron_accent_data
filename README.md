# INTRON HEALTH OPEN ACCESS DATASET FOR AFRICAN ACCENTS

Intron health promises to build africas first speech powered electronic medical record.
Current ASR models do not perform very well with african accent and this is due to the lack of diverse speech datasets that are are fully representative of anglophone african countries.

This project uses open access data to build a dataset of free speech that simulates a conversation between people, an interview or a speech.

## Running the Code

Clone the project

```bash
  git clone https://link-to-project
```

Install yt-dlp.\
on a linux VM do:
```bash
  brew install yt-dlp/taps/yt-dlp
```

Go to the project directory

```bash
  cd Intron_accent_data
```

Install dependencies

```bash
  conda env create -f requirements.yml
```

Go to Dataset directory

```bash
  cd dataset
```

Run the get_audio script to download youtube dataset

```bash
  chmod +x get_audio.sh
  ./get_audio.sh
```

Run the get_transcripts script to download data get_transcripts

```bash
  chmod +x get_transcripts.sh
  ./get_transcripts.sh
```

