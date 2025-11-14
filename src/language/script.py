import nltk
from nltk.tokenize import sent_tokenize
from deep_translator import GoogleTranslator

nltk.download('punkt_tab')


def translate(text: str):
    sentences = sent_tokenize(text)
    translator = GoogleTranslator(source='auto', target='ru')
    try:
        translations = translator.translate_batch(sentences)
    except Exception:
        return ''

    try:
        return ' '.join(translations)
    except Exception:
        return ''


if __name__ == '__main__':

    # text = "The QDBusUnixFileDescriptor class is used to hold one Unix file descriptor for use with the Qt D-Bus module. This allows applications to send and receive Unix file descriptors over the D-Bus connection, mapping automatically to the D-Bus type 'h'."

    # text = "Note that the file descriptor returned by this function is owned by the QDBusUnixFileDescriptor object and must not be stored past the lifetime of this object. It is ok to use it while this object is valid, but if one wants to store it for longer use, the file descriptor should be cloned using the Unix dup(2), dup2(2) or dup3(2) functions."

    text = "Generated-code classes also derive from QDBusAbstractInterface, all methods described here are also valid for generated-code classes. In addition to those described here, generated-code classes provide member functions for the remote methods, which allow for compile-time checking of the correct parameters and return values, as well as property type-matching and signal parameter-matching."

    sentences = sent_tokenize(text)

    # texts = [
    #     "The QDBusUnixFileDescriptor class is used to hold one Unix file descriptor for use with the Qt D-Bus module.",
    #     "This allows applications to send and receive Unix file descriptors over the D-Bus connection, mapping automatically to the D-Bus type 'h'.",
    # ]
    translator = GoogleTranslator(source='auto', target='ru')
    translations = translator.translate_batch(sentences)

    print(translations)
