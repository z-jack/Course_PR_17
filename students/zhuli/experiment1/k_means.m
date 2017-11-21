dim = 3; %ά��
k = input('k=');  
% PM=load('C:\\Users\����\\Downloads\\Course_PR_17-master\\experiment1\\data\\synthetic_data\\Aggregation.txt');
PM=load('C:\\Users\����\\Downloads\\Course_PR_17-master\\experiment1\\data\\synthetic_data\\flame.txt');
% PM=load('C:\\Users\����\\Downloads\\Course_PR_17-master\\experiment1\\data\\synthetic_data\\mix.txt');
% PM=load('C:\\Users\����\\Downloads\\Course_PR_17-master\\experiment1\\data\\synthetic_data\\R15.txt');
% PM=load('D:\\Matlab\\testSet.txt');
[N,M] = size(PM);
figure();%��������

CC = zeros(k,dim); % �������ľ���
D = zeros(N,k); % D(i,j)������i�;�������j�ľ���

%cell��Ԫ�����飬���ƽṹ�壬ÿ��Ԫ�ؿ��Բ�һ��
C = cell(1,k); % ��������ʼ������Ӧ�������������
for i = 1:k-1
    C{i} = [i];
end
C{k} = k:N;
B = 1:N; %�ϴε����У�����������һ���࣬���ֵΪ1
B(k:N) = k; %k��N���������ڵ�k��

%��ʼ���������ľ���,���ȡ
for i = 1:k
        n=randi(size(PM,1));
        CC(i,:)=PM(n,:);
end

%��ɫ����
A=[1,0,0;
    0,1,0;
    0,0,1;
    1,0,1;
    0,0,0;
    1,1,0;
    0,1,1;
    0.3,0.8,0.5;
    0.4,0.7,0.3;
    0.5,0.6,0.7;
    0.6,0.59,0.85;
    0.2,0.99,0.25;
    0.3,0.89,0.55;
    0.4,0.79,0.35;
    0.5,0.69,0.75;
    0.25,0.59,0.2;
    0.35,0.58,0.5;
    0.45,0.57,0.3;
    0.55,0.56,0.7;
    0.9,0.1,0.2;
    0.6,0.5,0.8;
    0.6,0.5,0.8;
    0.7,0.4,0.2;
    0.8,0.3,0.2;
    0.9,0.2,0.2;
    1,1,0.8;
    1,0.2,0.5;
    0.9,0.1,0.2;
    0.5,0.15,0.8;
    0.51,0.2,0.5;
    0.15,0.1,0.22;
    0.25,0.66,0.12;
    0.35,0.25,0.29;
    0.45,0.85,0.25];

while true   
    change = 0;
    %����i��k���������ĵľ���
    for i = 1:N
        for j = 1:k
              D(i,j) = sqrt((PM(i,1) - CC(j,1))^2 + (PM(i,2) - CC(j,2))^2);
        end
        t = find( D(i,:) == min(D(i,:)) ); % i���ڵ�t��
        if B(i) ~= t % �ϴε���i�����ڵ�t��
            change = 1;
            % ��i�ӵ�B(i)����ȥ��
            t1 = C{B(i)};
            t2 = find( t1==i );            
            t1(t2) = t1(1);
            t1 = t1(2:length(t1)); 
            C{B(i)} = t1;
            C{t} = [C{t},i]; % ��i�����t��
            B(i) = t;
        end        
    end
    if change == 0 
        break;
    end

    % ���¼���CC
    for i = 1:k
        CC(i,:) = 0;
        iclu = C{i};
        for j = 1:length(iclu)
            CC(i,:) = PM( iclu(j),: )+CC(i,:);
        end
        CC(i,:) = CC(i,:)/length(iclu);
    end
end

plot(CC(:,1),CC(:,2),'o') 
hold on

for i=1:N
    for x=1:k
        if(B(1,i)==x)
            plot3(PM(i,1),PM(i,2),PM(i,3),'.','markersize',15,'color',A(x,:));
             hold on
        end
    end
end
xlabel('X');
ylabel('Y');
zlabel('Z');
title('k-means');    