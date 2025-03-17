from flask import Flask,jsonify


todo = Flask('__name__')

@todo.route('/student-list')
def student_list():
    students = [
        {
            'id': 9,
            'student_name': 'egg',
            'age': 20,
            'email': 'ex@email'
        },
        {
            'id': 2,
            'student_name': 'horse',
            'age': 21,
            'email': 'horsy2@email'
        },
        {
            'id': 7,
            'student_name': 'gum',
            'age': 22,
            'email': 'glue3@email'
        }
    ]
    return jsonify(students)

@todo.route('/student-list/<int:id>')
def student_by_id(id):
    return jsonify({"message": f"Student ID received: {id}"})

    return jsonify(student)
if __name__=='__main__':

        todo.run(
            debug=True
        )