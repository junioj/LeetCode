# @param {String} s
# @param {String} t
# @return {Boolean}
def backspace_compare(s, t)
    a=0
    b=0
    while(s[a]!=nil)
        puts 's ' + a.to_s + ' ' + s[a]
        if(s[a]=='#')
            puts s
            puts s[a-1]
            puts s[a]
            if(a!=0)
                s[a-1]=''
                a=a-1
                s[a]=''
            else
                s[a]=''
            end
        else
            a = a+1
        end
    end
    
    while(t[b]!=nil)
        if(t[b]=='#')
            puts t
            puts t[b-1]
            puts t[b]
            # t.delete_at(t.index(b-1))
            if(b!=0)
                t[b-1]=''
                b=b-1
                t[b]=''
            else
                t[b]=''
            end
        else
            b = b+1
        end
    end
    
    puts 'strings:'
    puts 's ' + s
    puts 't ' + t
            
    if(s==t)
        # puts 'true'
        return true
    else
        return false
    end
end