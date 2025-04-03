﻿using System.Collections.Generic;
using OpenUtau.Api;
using OpenUtau.Core.Ustx;
using OpenUtau.Core.Voicevox;

namespace Voicevox {
    [Phonemizer("Simple Voicevox Japanese Phonemizer", "S-VOICEVOX JA", language: "JA")]
    public class SimpleVoicevoxPhonemizer : Phonemizer {

        protected VoicevoxSinger singer;

        public override void SetSinger(USinger singer) {
            this.singer = singer as VoicevoxSinger;
            if (this.singer != null) {
                this.singer.voicevoxConfig.Tag = this.Tag;
                VoicevoxUtils.Loaddic(this.singer);
            }
        }

        protected bool IsSyllableVowelExtensionNote(Note note) {
            return note.lyric.StartsWith("+~") || note.lyric.StartsWith("+*");
        }

        public override Result Process(Note[] notes, Note? prev, Note? next, Note? prevNeighbour, Note? nextNeighbour, Note[] prevNeighbours) {
            List<Phoneme> phonemes = new List<Phoneme>();
            for (int i = 0; i < notes.Length; i++) {
                var currentLyric = notes[i].lyric.Normalize(); //measures for Unicode

                Note[][] simplenotes = new Note[1][];
                var lyricList = notes[i].lyric.Split(" ");
                if (lyricList.Length > 1) {
                    notes[i].lyric = lyricList[1];
                }
                if (!IsSyllableVowelExtensionNote(notes[i])) {
                    if (VoicevoxUtils.IsHiraKana(notes[i].lyric)) {
                        phonemes.Add(new Phoneme { phoneme = notes[i].lyric });
                    } else if (VoicevoxUtils.IsPau(notes[i].lyric)) {
                        phonemes.Add(new Phoneme { phoneme = "R" });
                    } else if (VoicevoxUtils.dic.IsDic(notes[i].lyric)) {
                        phonemes.Add(new Phoneme { phoneme = VoicevoxUtils.dic.Lyrictodic(notes[i].lyric) });
                    } else {
                        phonemes.Add(new Phoneme { phoneme = "error"});
                    }
                }
            }
            return new Result { phonemes = phonemes.ToArray() };
        }
    }
}
