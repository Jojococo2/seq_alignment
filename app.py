from flask import Flask, jsonify, request
from Bio.Align import PairwiseAligner
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Sequence Alignment Tool</title>
               <link rel="stylesheet" type="text/css" href="/static/styles.css">

                <script>
                    async function submitForm(event) {
                        event.preventDefault();
                        const seq1 = document.getElementById('sequence1').value;
                        const seq2 = document.getElementById('sequence2').value;

                        const response = await fetch('/align', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ sequence1: seq1, sequence2: seq2 })
                        });

                        const data = await response.json();
                        document.getElementById('result').innerText = data.alignment || data.error;
                    }
                </script>
            </head>
            <body>
                <div class="container">
                    <h1>Sequence Alignment Tool</h1>
                    <form onsubmit="submitForm(event)">
                        <label for="sequence1">Sequence 1:</label>
                        <input type="text" id="sequence1" name="sequence1" required>
                        <br>
                        <label for="sequence2">Sequence 2:</label>
                        <input type="text" id="sequence2" name="sequence2" required>
                        <br>
                        <button type="submit">Align Sequences</button>
                    </form>
                    <div id="result" class="result"></div>
                </div>
            </body>
        </html>
    '''

@app.route('/align', methods=['POST'])
def align_sequences():
    data = request.json
    seq1 = data.get('sequence1')
    seq2 = data.get('sequence2')
    
    aligner = PairwiseAligner()
    alignments = aligner.align(seq1, seq2)
    alignment_result = str(alignments[0])
    
    return jsonify({'alignment': alignment_result})

if __name__ == '__main__':
    app.run(debug=True)

