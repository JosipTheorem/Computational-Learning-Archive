import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report





#(axis=0) (↓ column-wise sum)
#(axis=1) (→ row-wise sum)



def sample_gmm_2d(K, C, N, seed=None):
    """
    Generate K Gaussian components, each assigned randomly to one of C classes.
    Each component generates N samples.
    Returns:
      X  ... array of shape (K*N, 2)
      Y_ ... array of shape (K*N,)
    """
    if seed is not None:
        np.random.seed(seed)

    X = []
    Y_ = []

    for i in range(K):
       
        mu = np.random.uniform(-5, 5, 2)

        
        A = np.random.randn(2,2)
        cov = np.dot(A, A.T)  

        
        cls = np.random.randint(C)

       
        Xi = np.random.multivariate_normal(mu, cov, N)
        yi = np.full(N, cls)

        X.append(Xi)
        Y_.append(yi)

    X = np.vstack(X)
    Y_ = np.hstack(Y_)
    return X, Y_


def plot_decision_boundary(predict_fn, X, Y, steps=200, cmap="coolwarm"):
    x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
    y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, steps),
                         np.linspace(y_min, y_max, steps))
    
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = predict_fn(grid)
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=cmap)
    plt.scatter(X[:,0], X[:,1], c=Y, cmap=cmap, edgecolors="k")
    plt.show()
    #plt.savefig("(6,2,10)_[2,5,2].png")



def fcann2_train(X,Y_):
 
  X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    
  D = X.shape[1]
  C = np.max(Y_) + 1  # Broj klasa
  H = 5   # Dimenzija skrivenog sloja
########################################################################!!!!!!!!!!!!!!!!!!!
   # inicijaliziramo težine prema distribuciji koja je centrirana u nuli (npr. np.random.randn),
   #izbijelimo podatke tako da im oduzmemo srednju vrijednost i podijelimo ih sa standardnom devijacijom.
 ######################################################################!!!!!!!!!!!!!!!!!!
  np.random.seed(100)

  W1 = np.random.randn(H, D)  # Shape (C, N)
  W2 = np.random.randn(C, H)  # Shape (C, N)
  b1 = np.zeros((H, 1))  # Shape (C, 2)
  b2 = np.zeros((C, 1))  # Shape (C, 2)
    
  Y_onehot = np.zeros((C, K*N))  # Ista struktura kao P matrica
  Y_onehot[Y_, np.arange(K*N)] = 1 # One-hot

  param_niter = 100000
  param_delta = 0.05
  param_lambda=1e-3  

  # gradijentni spust (param_niter iteracija)
  for i in range(param_niter):

      ## NAPRIJED
      s1 = np.dot(W1,X.T) + b1
      h1 = np.maximum(0,s1)
      s2 = np.dot(W2,h1) + b2
      #exp_s2 =  np.exp(s2)
      exp_s2 = np.exp(s2 - np.max(s2, axis=0, keepdims=True))
      
      P = exp_s2/np.sum(exp_s2, axis=0, keepdims=True) ## tu su mi sve vjerojatnosti, znaci za svaki podatak za svaku klasu vjerojatnost
      P_yixi =  P[Y_, np.arange(K*N)] # ovdje P je vjerojatnost kojom model podatak xi klasificira u točan razred yi
      L = -np.sum(np.log(P_yixi))/(K*N) + param_lambda*(np.sum(W1**2) + np.sum(W2**2))

      if i % 10000 == 0:
        print(f"iter {i:6d}: loss = {L:.4f}")

      ## Računanje gradijenata širenjem unatrag (pogledati izvod za bolje razumijevanje), probati negdje pronaci bolju notaciju

      Gs2 = P - Y_onehot #(KN x C)
      
      grad_W2 = np.dot(Gs2, h1.T)/(K*N) + param_lambda*2*W2 #(C x H)
      grad_b2 = np.sum(Gs2, axis = 1, keepdims = True)/(K*N)

      Gh1 = np.dot(W2.T, Gs2) ##(KN x H)

      Gs1 = Gh1 * (s1>0) ### Element-wise

      grad_W1 = np.dot(Gs1, X)/(K*N) + param_lambda*2*W1 ##(H x D) 
      grad_b1 = np.sum(Gs1, axis = 1, keepdims = True)/(K*N)



      ############# poboljšani parametri
      
      W1 += -param_delta * grad_W1
      W2 += -param_delta * grad_W2
      b1 += -param_delta * grad_b1
      b2 += -param_delta * grad_b2
  
  return W1, W2, b1, b2


def fcann2_classify(X,W1,W2,b1,b2):
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

    s1 = np.dot(W1,X.T) + b1
    h1 = np.maximum(0,s1)
    s2 = np.dot(W2,h1) + b2
      #exp_s2 =  np.exp(s2)
    exp_s2 = np.exp(s2 - np.max(s2, axis=0, keepdims=True))
      
    P = exp_s2/np.sum(exp_s2, axis=0, keepdims=True) ## tu su mi sve vjerojatnosti, znaci za svaki podatak za svaku klasu vjerojatnost
    P_yixi =  P[Y_, np.arange(K*N)]

    return np.argmax(P, axis=0)
    

def fcann2_probabilities(X, W1, W2, b1, b2):
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    s1 = np.dot(W1, X.T) + b1
    h1 = np.maximum(0, s1)
    s2 = np.dot(W2, h1) + b2
    exp_s2 = np.exp(s2 - np.max(s2, axis=0, keepdims=True))
    P = exp_s2 / np.sum(exp_s2, axis=0, keepdims=True)
    return P



if  __name__ == "__main__":
    K = 6  # broj distribucija
    C = 2  # broj klasa
    N = 10 # broj po distribuciji


    
    np.random.seed(100)
    X, Y_ = sample_gmm_2d(K=K, C=C, N=N, seed=42)
    W1, W2, b1, b2 = fcann2_train(X,Y_)
    dec_fun = fcann2_classify(X, W1,W2, b1,b2)
  
    Y = fcann2_classify(X,W1,W2,b1,b2) 
    
    #dec_fun = lambda X: fcann2_probabilities(X, W1, W2, b1, b2)[1, :]  
    dec_fun = lambda X: fcann2_classify(X, W1, W2, b1, b2) 

    #probs = eval(ptlr, X)
    predicted_labels = Y

  # ispiši performansu (preciznost i odziv po razredima)
    accuracy = accuracy_score(Y_, predicted_labels)
    conf_mat = confusion_matrix(Y_, predicted_labels)
    report = classification_report(Y_, predicted_labels)

    print("Accuracy:", accuracy)
    print("Confusion matrix:\n", conf_mat)
    print("Classification report:\n", report)
  

    rect=(np.min(X, axis=0), np.max(X, axis=0))

    plot_decision_boundary(lambda X: fcann2_classify(X, W1, W2, b1, b2), X, Y_)

    #plt.savefig("(6,2,10)_[2,5,2].png")

