from flask import Flask, render_template, request, redirect, url_for, session, flash, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors, re, hashlib
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from flask_bcrypt import Bcrypt

app = Flask (__name__)

app.config['MYSQL_HOST']='sistemaro.mysql.dbaas.com.br'
app.config['MYSQL_USER']='sistemaro'
app.config['MYSQL_PASSWORD']= 'TW5brJ8Z!39X51'
app.config['MYSQL_DB']='sistemaro'

mysql = MySQL(app)

app.secret_key = 'mysecretkey'
app.permanent_session_lifetime = timedelta(seconds=10)

bcrypt = Bcrypt(app)
hashed_password = bcrypt.generate_password_hash

@app.route('/registroro', methods=['GET','POST'])
def site_ro():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM edital')
        itens = cur.fetchall()
        mysql.connection.commit()
        return render_template('index.html', nome=session['nome'], email=session['email'], editals = itens, dataUser = dataPerfilUsuario(), inforLogin = dataLoginSesion())
    return render_template("logincliente.html")


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename)  
        return render_template("text.html", name = f.filename)  
  



@app.route('/categoria')
def categoria():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM categorias')
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
    return render_template('index.html', categoria = itens)


@app.route('/final', methods=['GET','POST'] )
def final():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM final')
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
    return render_template('index.html', finals = itens)




@app.route('/status')
def status():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM status')
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
    return render_template('index.html', statuss = itens)


@app.route('/logout') 
def logout(): 
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('email', None) 
    return redirect(url_for('site_logincliente')) 


@app.route('/logouttt') 
def logouttt(): 
    session.pop('loggedin', None) 
    session.pop('id', None) 
    session.pop('email', None) 
    return redirect(url_for('site_login')) 
 

@app.route('/add_tt', methods=['POST'])
def add_tt():
    msg = ''
    if request.method == 'POST':
        nome                      = request.form['nome']
        telefone                    = request.form['telefone']
        email                       = request.form['email']
        senha                    = request.form['senha']
        setor                    = request.form['setor']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cadastro WHERE email = %s', (email,))
        account = cur.fetchone()
        cur.close()
          
        if account:
            flash('Email já cadastrado!')
        else:
            hash = senha + app.secret_key
            hash = hashlib.sha1(hash.encode())
            senha = hash.hexdigest()
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO cadastro (nome, telefone, email, senha, setor) VALUES (%s, %s, %s, %s, %s)', (nome, telefone, email, senha, setor))
            mysql.connection.commit()
            flash('Cadastro completo!')
    return redirect (url_for('site_cadastro'))



@app.route('/add_ro', methods=['POST'])
def add_ro():
    if request.method == 'POST':
        nome1                      = request.form['nome1']
        telefone1                    = request.form['telefone1']
        email                       = request.form['email']
        senha                    = request.form['senha']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cadastrotamtec WHERE email = %s', (email,))
        account = cur.fetchone()
        cur.close()
        if account:
            flash('Email já cadastrado!')
        else:
            senha_hash = generate_password_hash(senha, method='sha256')
            cur = mysql.connection.cursor()
            cur.execute('INSERT INTO cadastrotamtec (nome1, telefone1, email, senha) VALUES (%s, %s, %s, %s)', (nome1, telefone1, email, senha_hash))
            mysql.connection.commit()
            flash('Cadastro completo!')
    return redirect (url_for('site_cadastrotamtec'))



@app.route('/adicionar_registroro', methods=['POST'])
def adicionar_registroro():
    if request.method == 'POST':
        nomeprinc=request.form['nomeprinc']
        telprinc=request.form['telprinc']
        emailprinc=request.form['emailprinc']
        cargoprinc=request.form['cargoprinc']
        nome1princ=request.form['nome1princ']
        tel1princ=request.form['tel1princ']
        email1princ=request.form['email1princ']
        nome2princ=request.form['nome2princ']
        tel2princ=request.form['tel2princ']
        email2princ=request.form['email2princ']
        rsprinc=request.form['rsprinc']
        nomeprojprinc=request.form['nomeprojprinc']
        CNPJprinc=request.form['CNPJprinc']
        unidadeprinc=request.form['unidadeprinc']
        decisão=request.form['decisão']
        métricas=request.form['métricas']
        observaçãoprinc=request.form['observaçãoprinc']
        editalpubli = request.form['editalpubli']
        vendedor = request.form['vendedor']
        emailvendedor = request.form['emailvendedor']
        equipamento1 = request.form['equipamento1']
        equipamento2 = request.form['equipamento2']
        equipamento3 = request.form['equipamento3']
        equipamento4 = request.form['equipamento4']
        equipamento5 = request.form['equipamento5']
        equipamento6 = request.form['equipamento6']
        modelo1 = request.form['modelo1']
        modelo2 = request.form['modelo2']
        modelo3 = request.form['modelo3']
        modelo4 = request.form['modelo4']
        modelo5 = request.form['modelo5']
        modelo6 = request.form['modelo6']
        quantidade1 = request.form['quantidade1']
        quantidade2 = request.form['quantidade2']
        quantidade3 = request.form['quantidade3']
        quantidade4 = request.form['quantidade4']
        quantidade5 = request.form['quantidade5']
        quantidade6 = request.form['quantidade6']
        arquivoprinc = request.file['arquivoprinc'].read()
        cur = mysql.connection.cursor()
        arquivoprinc = request.files['arquivoprinc']
        cur.execute('INSERT INTO cadastroro (nomeprinc, telprinc, emailprinc, cargoprinc, nome1princ, tel1princ, email1princ, nome2princ, tel2princ, email2princ, rsprinc, nomeprojprinc, CNPJprinc, unidadeprinc, decisão, métricas, observaçãoprinc, editalpubli, vendedor, emailvendedor, equipamento1, equipamento2, equipamento3, equipamento4, equipamento5, equipamento6, modelo1, modelo2, modelo3, modelo4, modelo5, modelo6, quantidade1, quantidade2, quantidade3, quantidade4, quantidade5, quantidade6, arquivoprinc, arquivoprinc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s)', (nomeprinc, telprinc, emailprinc, cargoprinc, nome1princ, tel1princ, email1princ, nome2princ, tel2princ, email2princ, rsprinc, nomeprojprinc, CNPJprinc, unidadeprinc, decisão, métricas, observaçãoprinc, editalpubli, vendedor, emailvendedor, equipamento1, equipamento2, equipamento3, equipamento4, equipamento5, equipamento6, modelo1, modelo2, modelo3, modelo4, modelo5, modelo6, quantidade1, quantidade2, quantidade3, quantidade4, quantidade5, quantidade6, arquivoprinc, arquivoprinc))
        mysql.connection.commit()
        flash('RO adicionado com sucesso!')
        return redirect (url_for('site_ro'))


@app.route('/login', methods=['GET', 'POST'])
def site_login():
    msg = '' 
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form: 
        email = request.form['email'] 
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM cadastro WHERE email = % s AND senha = % s AND setor IN ("Processo", "Administrativo") ', (email, senha, )) 
        account = cursor.fetchone() 
        if account is not None: 
            session['loggedin'] = True
            session['id'] = account[5] 
            session['email'] = account[2] 
            session['nome'] = account[0] 
            session['telefone'] = account[1]
            session['senha'] = account[3] 
            session.permanent= True
            msg = 'Login confirmado!'
            return redirect (url_for('site_cliente'))
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form: 
        email = request.form['email'] 
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM cadastro WHERE email = % s AND senha = % s AND setor= "Vendas" ', (email, senha, )) 
        account = cursor.fetchone() 
        if account is not None: 
            session['loggedin'] = True
            session['id'] = account[5] 
            session['email'] = account[2] 
            session['nome'] = account[0] 
            session['telefone'] = account[1]
            session['senha'] = account[3] 
            session.permanent= True
            msg = 'Login confirmado!'
            return redirect (url_for('site_ro'))
        else:
            msg = 'Senha ou email invalidos!'
    return render_template("login.html",  msg = msg, dataUser = dataPerfilUsuario(), inforLogin = dataLoginSesion())


@app.route('/clientes')
def site_cliente():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cadastroro')
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
        return render_template('clientes.html', nome=session['nome'], cadastroros = itens, dataUser = dataPerfilUsuario(), inforLogin = dataLoginSesion())
    return render_template("login.html")


@app.route('/vendedores')
def sitevendedores():
    if 'loggedinC' in session:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM cadastroro')
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
        return render_template('RO.html', nome=session['nome1'], cadastroros = itens, dataUserC = dataPerfilUsuarioC(), inforLoginC = dataLoginSesionC())
    return render_template("logincliente.html")



@app.route('/rovendedor')
def siterovendedor():
    if 'loggedinC' in session: 
        cur = mysql.connection.cursor()
        cur.execute('SELECT emailvendedor FROM cadastroro WHERE emailvendedor = {} ')
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
        return render_template('revendedor.html', nome1=session['nome1'], cadastroros = itens, dataUserC = dataPerfilUsuarioC(), inforLoginC = dataLoginSesionC())
    return render_template("logincliente.html")



@app.route('/logincliente', methods=['GET', 'POST'])
def site_logincliente():
    msg = '' 
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form: 
        email = request.form['email'] 
        senha = request.form['senha']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM cadastrotamtec WHERE email = % s AND senha= % s', (email, senha,)) 
        account = cursor.fetchone()
        if account :
            session['loggedinC'] = True
            session['id'] = account[4] 
            session['email'] = account[2] 
            session['nome1'] = account[0] 
            session['telefone1'] = account[1]
            session['senha'] = account[3]
            session.permanent = True
            msg = 'Login confirmado!'
            return redirect (url_for('site_ro'))
        else: 
            msg = 'Senha ou email invalidos!'
    return render_template("logincliente.html",  msg = msg, dataUserc = dataPerfilUsuarioC(), inforLoginc = dataLoginSesionC())


@app.route('/acesso')
def site_acesso():
    if 'loggedin' in session:
        return render_template('acesso.html', nome=session['nome'],telefone=session['telefone'], email=session['email'], senha=session['senha'], id=session['id'])
    return render_template('login.html')


@app.route('/acessocliente')
def site_acessocliente():
    if 'loggedinC' in session:
        return render_template('acessocliente.html', nome1=session['nome1'],telefone1=session['telefone1'], email=session['email'], senha=session['senha'], id=session['id'])
    return render_template('logincliente.html')


def dataLoginSesion():
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form and 'nome' in request.form and 'telefone' in request.form:
        id = request.form['id'] 
        email = request.form['email'] 
        senha = request.form['senha'] 
        nome = request.form['nome'] 
        telefone = request.form['telefone'] 
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cadastro WHERE id='%s'" % (id, email, senha, nome, telefone))
        inforLogin = cursor.fetchone() 
        if inforLogin:
            session['loggedin'] = True
            session['id'] = inforLogin[5] 
            session['email'] = inforLogin[2] 
            session['senha'] = inforLogin[3] 
            session['nome'] = inforLogin[0] 
            session['telefone'] = inforLogin[1] 
            session.permanent = True
        return inforLogin



def dataLoginSesionC():
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form and 'nome1' in request.form and 'telefone1' in request.form:
        id = request.form['id'] 
        email = request.form['email'] 
        senha = request.form['senha'] 
        nome1 = request.form['nome1'] 
        telefone1 = request.form['telefone1'] 
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cadastrotamtec WHERE id='%s'" % (id, email, senha, nome1, telefone1))
        inforLoginc = cursor.fetchone() 
        if inforLoginc:
            session['loggedinC'] = True
            session['id'] = inforLoginc[4] 
            session['email'] = inforLoginc[2] 
            session['senha'] = inforLoginc[3] 
            session['nome1'] = inforLoginc[0] 
            session['telefone1'] = inforLoginc[1] 
            session.permanent = True
        return inforLoginc



def dataPerfilUsuario():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM cadastro WHERE id='%s'" % (id,))
    datosUsuario = cursor.fetchone() 
    return datosUsuario


def dataPerfilUsuarioC():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM cadastrotamtec WHERE id='%s'" % (id,))
    datosUsuarioc = cursor.fetchone() 
    return datosUsuarioc



@app.route('/cadastrotamtec', methods=['GET', 'POST'])
def site_cadastrotamtec():
    return render_template("cadastrotamtec.html")


@app.route('/codigo', methods=['GET', 'POST'])
def site_codigo():
    return render_template("código.html")


@app.route('/cadastro', methods=['GET', 'POST'])
def site_cadastro():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM setor')
    itens = cur.fetchall()
    print(itens)
    mysql.connection.commit()
    return render_template("cadastro.html", setors = itens)



@app.route('/delete/<string:id>')
def site_delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cadastroro WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Deletado com sucesso')
    return redirect(url_for('site_ro'))



@app.route('/deleteacesso', methods=['POST'])
def deleteacesso():
    if request.method == 'POST' and'loggedinC' in session:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM cadastrotamtec WHERE id = {0}".format(session['id']))
        mysql.connection.commit()
        msg ='Dados deletados!'
        return render_template('logincliente.html', msg=msg)
    else:
        msg ='Dados não deletados!'
        return render_template('logincliente.html', msg=msg)


@app.route('/deleteacessott', methods=['POST'])
def deleteacessott():
    if request.method == 'POST' and'loggedin' in session:
       
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM cadastro WHERE id = {0}".format(session['id']))
        mysql.connection.commit()
        msg ='Dados deletados!'
        return render_template('login.html', msg=msg)
    else:
        msg ='Dados não deletados!'
        return render_template('login.html', msg=msg)


@app.route('/edit/<id>')
def site_edit(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cadastroro WHERE id = {0}'.format(id))
    data = cur.fetchall()
    return render_template('editarro.html', cadastroro = data[0])


@app.route('/ros', methods=['POST'])
def ros():
    if 'loggedinC' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cadastroro WHERE emailvendedor= '{}' ")
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
        return render_template('RO.html', nome1=session['nome1'], cadastroros = itens, dataUserC = dataPerfilUsuarioC(), inforLoginC = dataLoginSesionC())
    return render_template("logincliente.html")


@app.route('/recusado', methods=['GET','POST'])
def recusado():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cadastroro WHERE status IN ('Recusado', 'Negado') OR retorno IN ('Prazo excedido', 'Em análise')")
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
        return render_template('recusado.html', nome=session['nome'], cadastroros = itens, dataUser = dataPerfilUsuario(), inforLogin = dataLoginSesion())
    return render_template("login.html")


@app.route('/aprovado', methods=['GET','POST'])
def aprovado():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cadastroro WHERE status='Aprovado'")
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
        return render_template('aprovado.html', nome=session['nome'], cadastroros = itens, dataUser = dataPerfilUsuario(), inforLogin = dataLoginSesion())
    return render_template("login.html")


@app.route('/finalizado', methods=['GET','POST'])
def finalizado():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM cadastroro WHERE statusfinal='Finalizado' ")
        itens = cur.fetchall()
        print(itens)
        mysql.connection.commit()
        return render_template('finalizado.html', nome=session['nome'], cadastroros = itens, dataUser = dataPerfilUsuario(), inforLogin = dataLoginSesion())
    return render_template("login.html")


@app.route('/pdf/<id>')
def site_pdf(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cadastroro WHERE id = {0}'.format(id))
    data = cur.fetchall()
    return render_template('pdfro.html', cadastroro = data[0])



@app.route('/update/<id>', methods=['POST'])
def site_update(id):
    if request.method == 'POST':
        equipamento1 = request.form['equipamento1']
        equipamento2 = request.form['equipamento2']
        equipamento3 = request.form['equipamento3']
        equipamento4 = request.form['equipamento4']
        equipamento5 = request.form['equipamento5']
        equipamento6 = request.form['equipamento6']
        modelo1 = request.form['modelo1']
        modelo2 = request.form['modelo2']
        modelo3 = request.form['modelo3']
        modelo4 = request.form['modelo4']
        modelo5 = request.form['modelo5']
        modelo6 = request.form['modelo6']
        quantidade1 = request.form['quantidade1']
        quantidade2 = request.form['quantidade2']
        quantidade3 = request.form['quantidade3']
        quantidade4 = request.form['quantidade4']
        quantidade5 = request.form['quantidade5']
        quantidade6 = request.form['quantidade6']
        status = request.form['status']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE cadastroro
            SET equipamento1 = %s,
                equipamento2 = %s,
                equipamento3 = %s,
                equipamento4 = %s,
                equipamento5 = %s,
                equipamento6 = %s,
                modelo1 = %s,
                modelo2 = %s,
                modelo3 = %s,
                modelo4 = %s,
                modelo5 = %s,
                modelo6 = %s,
                quantidade1 = %s,
                quantidade2 = %s,
                quantidade3 = %s,
                quantidade4 = %s,
                quantidade5 = %s,
                quantidade6 = %s,
                status = %s
            WHERE id = %s
        """, (equipamento1, equipamento2, equipamento3, equipamento4, equipamento5, equipamento6, modelo1, modelo2, modelo3, modelo4, modelo5, modelo6, quantidade1, quantidade2, quantidade3, quantidade4, quantidade5, quantidade6, status, id))
        mysql.connection.commit()
        msg ='Dados atualizados'
        return redirect(url_for('site_cliente', msg=msg))
    
    
@app.route('/updatefinal/<id>', methods=['POST'])
def site_updatefinal(id):
    if request.method == 'POST':
        data = request.form['data']
        nro = request.form['nro']
        nro2 = request.form['nro2']
        statusro = request.form['statusro']
        statusro2 = request.form['statusro2']
        brand = request.form['brand']
        brand2 = request.form['brand2']
        obsfinal = request.form['obsfinal']
        responsavel = request.form['responsavel']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE cadastroro
            SET data = % s,
                nro = % s,
                nro2 = % s,
                statusro = % s,
                statusro2 = % s,
                brand = % s,
                brand2 = % s,
                obsfinal = % s,
                responsavel = % s
                
            WHERE id = %s
        """, (data, nro, nro2, statusro, statusro2, brand, brand2, obsfinal, responsavel, id))
        mysql.connection.commit()
        msg ='Dados atualizados'
        return redirect(url_for('site_cliente', msg=msg))
    

@app.route('/updatereq/<id>', methods=['POST'])
def site_updatereq(id):
    if request.method == 'POST':
        requerimento = request.form['requerimento']
        retorno = request.form['retorno']
        novonro = request.form['novonro']
        novadata = request.form['novadata']
        novarodata = request.form['novarodata']
        novonro1 = request.form['novonro1']
        novadata1 = request.form['novadata1']
        novarodata1 = request.form['novarodata1']
        novonro2 = request.form['novonro2']
        novadata2 = request.form['novadata2']
        novarodata2 = request.form['novarodata2']
        novonro3 = request.form['novonro3']
        novadata3 = request.form['novadata3']
        novarodata3 = request.form['novarodata3']
        novonro4 = request.form['novonro4']
        novadata4 = request.form['novadata4']
        novarodata4 = request.form['novarodata4']
        novonro5 = request.form['novonro5']
        novadata5 = request.form['novadata5']
        novarodata5 = request.form['novarodata5']
        novonro6 = request.form['novonro6']
        novadata6 = request.form['novadata6']
        novarodata6 = request.form['novarodata6']
        novonro7 = request.form['novonro7']
        novadata7 = request.form['novadata7']
        novarodata7 = request.form['novarodata7']
        novonro8 = request.form['novonro8']
        novadata8 = request.form['novadata8']
        novarodata8 = request.form['novarodata8']
        novonro9 = request.form['novonro9']
        novadata9 = request.form['novadata9']
        novarodata9 = request.form['novarodata9']
        novonro10 = request.form['novonro10']
        novadata10 = request.form['novadata10']
        novarodata10 = request.form['novarodata10']
        novonro11 = request.form['novonro11']
        novadata11 = request.form['novadata11']
        novarodata11 = request.form['novarodata11']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE cadastroro
            SET requerimento = % s,
                retorno = % s,
                novonro = % s,
                novadata = % s,
                novarodata = % s,
                novonro1 = % s,
                novadata1 = % s,
                novarodata1 = % s,
                novonro2 = % s,
                novadata2 = % s,
                novarodata2 = % s,
                novonro3 = % s,
                novadata3 = % s,
                novarodata3 = % s,
                novonro4 = % s,
                novadata4 = % s,
                novarodata4 = % s,
                novonro5 = % s,
                novadata5 = % s,
                novarodata5 = % s,
                novonro6 = % s,
                novadata6 = % s,
                novarodata6 = % s,
                novonro7 = % s,
                novadata7 = % s,
                novarodata7 = % s,
                novonro8 = % s,
                novadata8 = % s,
                novarodata8 = % s,
                novonro9 = % s,
                novadata9 = % s,
                novarodata9 = % s,
                novonro10 = % s,
                novadata10 = % s,
                novarodata10 = % s,
                novonro11 = % s,
                novadata11 = % s,
                novarodata11 = % s
            WHERE id = %s
        """, (requerimento, retorno, novonro, novadata, novarodata, novonro1, novadata1, novarodata1, novonro2, novadata2, novarodata2, novonro3, novadata3, novarodata3, novonro4, novadata4, novarodata4, novonro5, novadata5, novarodata5, novonro6, novadata6, novarodata6, novonro7, novadata7, novarodata7, novonro8, novadata8, novarodata8, novonro9, novadata9, novarodata9, novonro10, novadata10, novarodata10, novonro11, novadata11, novarodata11, id))
        mysql.connection.commit()
        msg ='Dados atualizados'
        return redirect(url_for('site_cliente', msg=msg))
    


@app.route('/updatedados', methods=['GET','POST'])
def site_updatedados():
    if request.method == 'POST' and'loggedin' in session:
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        senha = request.form['senha']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE cadastro
            SET nome = %s,
                telefone = %s,
                email = %s,
                senha = %s
            WHERE id = %s
        """, (nome, telefone, email, senha, session['id']))
        mysql.connection.commit()
        msg ='Dados atualizados'
        return render_template('login.html', msg=msg)
    else:
        msg ='Dados não atualizados'
        return render_template('login.html', msg=msg)
   
   
@app.route('/updatedadoscliente', methods=['GET','POST'])
def site_updatedadoscliente():
    if request.method == 'POST' and'loggedinC' in session:
        nome1 = request.form['nome1']
        email = request.form['email']
        telefone1 = request.form['telefone1']
        senha = request.form['senha']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE cadastrotamtec
            SET nome1 = %s,
                telefone1 = %s,
                email = %s,
                senha = %s
            WHERE id = %s
        """, (nome1, telefone1, email, senha, session['id']))
        mysql.connection.commit()
        msg ='Dados atualizados'
        return render_template('logincliente.html', msg=msg)
    else:
        msg ='Dados não atualizados'
        return render_template('logincliente.html', msg=msg) 
    
    
@app.route('/alterar/<id>')
def site_alterar(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cadastrotamtec')
    data = cur.fetchall()
    return render_template('acesso.html', cadastrott = data[0])


@app.route('/senha')
def site_senha():
    return render_template("senha.html")


@app.route('/redefinirsenha')
def site_redsenha():
    return render_template("redefinirsenha.html")


@app.route('/forgotpassword', methods=['GET','POST'])
def site_forgotsenha():
    return render_template("forgotpassword.html")


@app.route('/finalizar')
def site_finalizar():
    return render_template("adicionarro.html")

if __name__ == "__main__":
    with app.app_context():
        mysql.create_all()
        app.run(debug=True)