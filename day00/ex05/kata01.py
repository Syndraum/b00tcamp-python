def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for i in languages:
        print(i, "was created by", languages[i])


if __name__ == "__main__":
    main()
